from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import Post, Comment


class Admin(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and getattr(user.role, 'name', None) in ['Admin', 'Moderator']


class OwnerorReadonly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        if isinstance(obj, Post):
            return obj.author == request.user
        elif isinstance(obj, Comment):
            return obj.author == request.user
        return False
