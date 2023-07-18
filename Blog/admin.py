from django.contrib import admin
from .models import Blog, Index, EnglishWords, EnglishRules, PythonQuestion, Category, RulesOfEnglish

admin.site.register(Blog)
admin.site.register(Index)
admin.site.register(Category)
admin.site.register(EnglishRules)
admin.site.register(PythonQuestion)
admin.site.register(RulesOfEnglish)

@admin.register(EnglishWords)
class EnglishWordsAdmin(admin.ModelAdmin):
    list_display = ('word', 'translate', 'rules', 'category')
    #Поля видимые в админке (метод STR уже не будет работать)
    list_editable = ('translate', 'rules', 'category')
    #поля которые можно редактировать(кроме первого, это ссылка)
    ordering = ('word',)
    #сортировка таблицы, можно поставить второй атрибут
    list_per_page = 50
    #логику включи
    filter_horizontal = ('rule',)
    #отображение МениТуМени полей в админке



