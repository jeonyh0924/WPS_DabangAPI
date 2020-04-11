from rest_framework import serializers

from .models import PostTest


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostTest
        # fields = '__all__'
        fields = (
            'testtitle',
            'testdesc',
            'pk',
        )