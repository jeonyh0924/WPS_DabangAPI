import json

import requests
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action

from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings

from members.models import SocialLogin, RecentlyPostList
from members.serializers import UserSerializer, UserProfileSerializer
from posts.models import PostRoom
from posts.serializers import PostListSerializer

User = get_user_model()
JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class UserModelViewSet(viewsets.ModelViewSet):
    """
    viewsets.ModelViewSet 특징
    'list', 'create', 'retrieve', 'update', 'destroy' 기능 자동 지원, 별도의 함수 작성 가능 api코드 간소화

    # 함수들을 오버라이딩 하는 경우 상속받는 기능의 코드를 이해한 상태에서 건드려야 생산성과 유지보수의 이점을 둘 다 가져가는 듯 하다.
    # 각 함수를 오버라이딩 할 때 어떤 모듈의 함수인지 이해하는 지식 필요할 듯

    추후 추가할 기능들
     - 유저 프로필 페이지 최근 본 게시글 목록, 찜한 게시글 목록
     - 회원가입 시 유저 아이디 중복 체크
     - 유저 패스워드 변경
     - 특정 상황에 따른 푸쉬알림
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_serializer_class(self):
        if self.action in "create":
            serializer_class = UserSerializer
            return serializer_class
        else:
            serializer_class = UserProfileSerializer
            return serializer_class

    def get_permissions(self):
        if self.action == ("retrieve", "partial_update", "update", "destroy"):
            permission_classes = [IsAuthenticated()]
            return permission_classes
        elif self.action == "list":
            # 모든 유저의 목록을 보여주고 싶지 않아서
            permission_classes = [IsAdminUser()]
            return permission_classes
        else:
            permission_classes = [AllowAny()]
            return permission_classes

    @action(detail=False, methods=['POST'])
    def jwt(self, request):
        username = request.POST.get('username')
        userpass = request.POST.get('password')
        user = authenticate(username=username, password=userpass)
        payload = JWT_PAYLOAD_HANDLER(user)
        jwt_token = JWT_ENCODE_HANDLER(payload)
        if user is not None:
            data = {
                'jwt': jwt_token,
                'user': UserSerializer(user).data
            }
            return Response(data)


class KakaoJwtTokenView(APIView):
    def post(self, request):
        access_token = request.data.get('accessToken')
        url = 'https://kapi.kakao.com/v2/user/me'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
        }
        kakao_response = requests.post(url, headers=headers)

        user_data = kakao_response.json()
        kakao_id = user_data['id']
        user_username = user_data['properties']['nickname']
        user_first_name = user_username[1:]
        user_last_name = user_username[0]
        try:
            user = User.objects.get(username=kakao_id)
        except User.DoesNotExist:
            user = User.objects.create_user(
                username=kakao_id,
                first_name=user_first_name,
                last_name=user_last_name,

            )
        payload = JWT_PAYLOAD_HANDLER(user)
        jwt_token = JWT_ENCODE_HANDLER(payload)

        kakao = SocialLogin.objects.filter(type='kakao')[0]
        user.social.add(kakao)
        data = {
            'token': jwt_token,
            'user': UserSerializer(user).data,
        }

        return Response(data)


class FacebookJwtToken(APIView):
    api_base = 'https://graph.facebook.com/v3.2'
    api_get_access_token = f'{api_base}/oauth/access_token'
    api_me = f'{api_base}/me'

    def post(self, request):
        access_token = request.data.get('accessToken')
        params = {
            'access_token': access_token,
            'fields': ','.join([
                'id',
                'first_name',
                'last_name',
                'picture.type(large)',
            ])
        }
        response = requests.get(self.api_me, params)
        data = response.json()

        facebook_id = data['id']
        first_name = data['first_name']
        last_name = data['last_name']

        try:
            user = User.objects.get(username=facebook_id)
        except User.DoesNotExist:
            user = User.objects.create_user(
                username=facebook_id,
                first_name=first_name,
                last_name=last_name,
            )
        payload = JWT_PAYLOAD_HANDLER(user)
        jwt_token = JWT_ENCODE_HANDLER(payload)
        facebook = SocialLogin.objects.filter(type='facebook')[0]
        user.social.add(facebook)
        data = {
            'token': jwt_token,
            'user': UserSerializer(user).data,
        }
        return Response(data)


class recentlyPostListView(APIView):
    def get(self, request):
        post = request.data.get('post')

        post = int(post)
        post = PostRoom.objects.get(pk=post)
        relation = RecentlyPostList.objects.get(
            
        )
        while True:
            social_user = RecentlyPostList.objects.filter(user=request.user.pk)
            user_post_count = len(social_user)

            if user_post_count >= 5:
                social_user[0].delete()
            else:
                break
        RecentlyPostList.objects.create(
            user=request.user,
            post=post,
        )
        social_user = RecentlyPostList.objects.filter(user=request.user.pk)
        print(social_user)
        data = {
            # "User & Post relation": social_user,
            "message": "최근 유저 정보 리스트에 추가되었습니다."
        }
        return Response(data, status=status.HTTP_200_OK)
# class socialLogin(APIView):
#     def post(self, request):
#         local_host = 'http://localhost:8000'
#         deploy_host = 'https://moonpeter.com'
#         url = f'{local_host}/auth/convert-token'
#         token = request.data.get('token')
#         social_type = request.data.get('type')
#         if social_type:
#             if social_type == 'facebook':
#                 client_id = FACEBOOK_APP_ID
#                 client_pass = FACEBOOK_APP_SECRET
#             elif social_type == 'kakao':
#                 client_id = KAKAO_APP_ID
#
#         params = {
#             "grant_type": "convert_token",
#             "client_id": f"{client_id}",
#             "backend": f'{social_type}',
#             "token": f'{token}'
#         }
#         if social_type == 'facebook':
#             params["client_secret"] = client_pass
#
#         response = requests.post(url, params=params)
#
#         response_json = response.json()
#
#         data = {
#             'res': response_json,
#         }
#         return Response(data, status=status.HTTP_200_OK)
