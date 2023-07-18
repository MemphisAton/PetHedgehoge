"""
URL configuration for My_pet_hedgehog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from My_pet_hedgehog import settings

admin.site.site_header = "Администрирование ЖЖ"
admin.site.index_title = 'Админка'
admin.site.site_title = 'ЖЖ'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#какая то хрень связанная с картинкамию Разобраться позже
    
#handler404 = pageNotFound

