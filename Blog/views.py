from django.shortcuts import render
from Blog.models import Blog
from random import sample


def index(request):
    data = [{'image': 'blog photo',
             'name': 'My blog',
             'about': 'тут будет храниться описание моих будней'},
            {'image': 'me photo',
             'name': 'About me',
             'about': 'тут будет храниться описание меня'},
            {'image': 'pass1',
             'name': 'pass1',
             'about': 'pass1'}]
    posts = sample(list(Blog.objects.all()), 3)

    return render(request, 'Blog/index.html', {'data': data, 'posts': posts})


def all_posts(request):
    posts = list(Blog.objects.all())
    return render(request, 'Blog/all_posts.html', {'posts': posts})
