from django.db import models


# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} from {str(self.time_create)[:11]}'


class Index(models.Model):
    name = models.CharField(max_length=255)
    about = models.CharField(max_length=255)
    image = models.ImageField(upload_to='photos/db')
    url = models.CharField(max_length=111, default='blog_index')


class EnglishWords(models.Model):
    word = models.CharField(max_length=20, unique=True)
    translate = models.CharField(max_length=100)
    rules = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.word}'


class EnglishRules(models.Model):
    rules = models.CharField(max_length=255)
    content = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.rules}'


class PythonQuestion(models.Model):
    subject = models.CharField(max_length=255)
    description = models.TextField(null='True', blank=True)
    need = models.BooleanField(default=False)

    def __str__(self):
        if self.need is False:
            return f'Тема для изучения {self.subject} (статус - неизучено)'
        return f'Тема для изучения {self.subject} (статус - изучено)'
