from django.apps import AppConfig

class PostsConfig(AppConfig):
    """
    Configuration for the Posts application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
