from django.shortcuts import get_object_or_404
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import (UserListCreate, UserDetail, PostListCreate, CommentListCreate)

urlpatterns = [    
    # User endpoints
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    
    # Post endpoints
    path('posts/', PostListCreate.as_view(), name='post-list-create'),
    
    # Comment endpoints
    path('comments/', CommentListCreate.as_view(), name='comment-list-create'),
    
    # Authentication endpoint
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
