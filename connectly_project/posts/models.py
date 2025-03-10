from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):  
    email = models.EmailField(unique=True)  
    username = models.CharField(max_length=150, unique=True)  
    password = models.CharField(max_length=128)  # Explicitly define password

    def set_password(self, raw_password):  
        from django.contrib.auth.hashers import make_password  
        self.password = make_password(raw_password)

    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Post(models.Model):
    """
    Represents a post created by a user.
    """
    content = models.TextField(blank=False)
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='posts'
    )
    liked_by = models.ManyToManyField(
        User, 
        related_name='liked_posts', 
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.author.username} at {self.created_at}" 


class Comment(models.Model):
    """
    Represents a comment made on a post by a user.
    """
    text = models.TextField(blank=False)
    author = models.ForeignKey(
        User, 
        related_name='comments', 
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post, 
        related_name='comments', 
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on Post {self.post.id}"
