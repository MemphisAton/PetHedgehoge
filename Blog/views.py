from django.shortcuts import render
from Blog.models import Blog, Index
from random import sample


def index(request):
    posts = sample(list(Blog.objects.all()), 3)
    data = Index.objects.all()
    return render(request, 'Blog/index.html', {'data': data, 'posts': posts})


def all_posts(request):
    posts = Blog.objects.all()[::-1]
    return render(request, 'Blog/all_posts.html', {'posts': posts})

