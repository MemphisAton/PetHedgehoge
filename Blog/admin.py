from django.contrib import admin

# Register your models here.

from .models import Blog, Index, EnglishWords, EnglishRules, PythonQuestion


admin.site.register(Blog)
admin.site.register(Index)
admin.site.register(EnglishWords)
admin.site.register(EnglishRules)
admin.site.register(PythonQuestion)