from django.urls import path, include
from .views import index, all_posts

urlpatterns = [
    path('', index, name='blog_index'),
    path('posts/', all_posts, name='blog_all_posts')
]