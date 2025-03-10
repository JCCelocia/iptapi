from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import Post, Comment


class IsAdminOrModerator(BasePermission):
# Grants access to users with Admin or Moderator roles.
# Requires the User model to have a 'role' field with a 'name' attribute.

    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and getattr(user.role, 'name', None) in ['Admin', 'Moderator']


class IsOwnerOrReadOnly(BasePermission):
# Allows read-only access to all users but restricts modifications to the object's owner.
# Assumes the model instance includes an 'author' attribute.

    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request.
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        if request.user.is_superuser:
            return True
        # Otherwise, the user must be the owner.
        if isinstance(obj, Post):
            return obj.author == request.user
        elif isinstance(obj, Comment):
            return obj.author == request.user
        return False
