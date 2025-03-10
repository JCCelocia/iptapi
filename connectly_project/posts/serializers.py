from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User, Post, Comment

class UserSerializer(serializers.ModelSerializer):
    """
    Serializes User model data, enforcing unique constraints on username and email.
    """
    liked_posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    email = serializers.EmailField(
        error_messages={
            'blank': 'Email is required.',
            'max_length': 'Email must be 50 characters or less.',
            'unique': 'This email already exists.'
        }
    )
    username = serializers.CharField(
        error_messages={
            'blank': 'Username is required.',
            'max_length': 'Username must be 50 characters or less.',
        },
        validators=[UniqueValidator(queryset=User.objects.all(), message='Username already exists.')]
    )
    
    def validate_username(self, value):
        if not value.isalnum():
            raise serializers.ValidationError("Username must contain only alphanumeric characters.")
        return value

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'liked_posts', 'created_at']


class PostSerializer(serializers.ModelSerializer):
    """
    Serializes Post model data, linking related comments.
    """
    comments = serializers.StringRelatedField(many=True, read_only=True)
    content = serializers.CharField(
        error_messages={'blank': 'Content is required and cannot be empty.'}
    )
    author = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        error_messages={
            'required': 'Author is required.',
            'does_not_exist': 'User with the given ID does not exist.'
        }
    )
    
    class Meta:
        model = Post
        fields = ['id', 'content', 'author', 'created_at', 'comments']


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializes Comment model data while linking related post and author.
    """
    text = serializers.CharField(
        error_messages={'blank': 'Text is required and cannot be empty.'}
    )
    author = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        error_messages={
            'required': 'Author is required.',
            'does_not_exist': 'Author with the given ID does not exist.'
        }
    )
    post = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all(),
        error_messages={
            'required': 'Post is required.',
            'does_not_exist': 'Post with the given ID does not exist.'
        }
    )
    post_content = serializers.CharField(source='post.content', read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'text', 'author', 'post', 'post_content', 'created_at']
