from django.shortcuts import render


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

    return render(request, 'Blog/index.html', {'data': data})


# class BlogEntries(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField(blank=True)
#     photo = models.ImageField(upload_to='')
#     time_create = models.DateTimeField(auto_now_add=True)
#     time_update = models.DateTimeField(auto_now=True)
#     name = models.CharField(max_length=11, default='qwerty')