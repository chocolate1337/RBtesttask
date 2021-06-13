from django.contrib import admin
from .models import Author, Article


class AdminAuthor(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['name']


class AdminArticle(admin.ModelAdmin):
    fields = ('authors', 'title', 'text')
    list_filter = ['authors']


admin.site.register(Article, AdminArticle)
admin.site.register(Author, AdminAuthor)
