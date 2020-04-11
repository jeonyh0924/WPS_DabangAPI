from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models import PostRoom, PostTest
from posts.serializers import PostListSerializer


class PostList(APIView):
    # 게시물 생성 : /posts/
    def post(self, request, format=None):
        serializer = PostListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 게시물 조회 : /posts/
    def get(self, request, format=None):
        queryset = PostTest.objects.all()
        serializer = PostListSerializer(queryset, many=True)
        return Response(serializer.data)


class PostDetail(APIView):
    def get_object(self, pk):
        try:
            return PostTest.objects.get(pk=pk)
        except PostTest.DoesNotExist:
            raise Http404

    # 특정 게시물 조회 : /posts/{pk}/
    def get(self, request, pk):
        posttest = self.get_object(pk)
        serializer = PostListSerializer(posttest)
        return Response(serializer.data)

    # 특정 게시물 수정 : /posts/{pk}/
    def put(self, request, pk, format=None):
        posttest = self.get_object(pk)
        serializer = PostListSerializer(posttest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 특정 게시물 삭제 : /posts/{pk}/
    def delete(self, request, pk, format=None):
        posttest = self.get_object(pk)
        posttest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)