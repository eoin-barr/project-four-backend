from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post, Comment

User = get_user_model()

class BasicPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'


class NestedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'profile_image', 'followed_by')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PopulatedCommentSerializer(CommentSerializer):
    owner = NestedUserSerializer()


class PostDetailSerializer(serializers.ModelSerializer):
    comments = PopulatedCommentSerializer(many=True, read_only=True)
    saved_by = NestedUserSerializer(many=True, read_only=True)
    owner = NestedUserSerializer(read_only=True)
    
    class Meta:
        model = Post
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    comments = PopulatedCommentSerializer(many=True, read_only=True)
    saved_by = NestedUserSerializer(many=True, read_only=True)
    owner = NestedUserSerializer(read_only=True)
    value = serializers.CharField(source='title')
    label = serializers.CharField(source='title')

    class Meta:
        model = Post
        fields = '__all__'


class UserPostDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'image')
