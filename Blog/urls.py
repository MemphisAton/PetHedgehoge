from django.conf.urls.static import static
from django.urls import path, include

from My_pet_hedgehog import settings
from .views import index, all_posts, test_page

urlpatterns = [
    path('', index, name='blog_index'),
    path('posts/', all_posts, name='blog_all_posts'),
    path('test/', test_page, name='test_page')
]  # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

