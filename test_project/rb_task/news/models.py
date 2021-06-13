from random import randint

from django.db import models
from django.db.models import Count


class RandomManager(models.Manager):
    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return self.all()[random_index]


class Author(models.Model):
    name = models.CharField(max_length=20, null=False, verbose_name='Имя')
    objects = RandomManager()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'author'
        ordering = ['name']


class Article(models.Model):
    title = models.CharField(max_length=100, null=False, verbose_name='Заголовок')
    text = models.CharField(max_length=2000, null=False, verbose_name='Текст статьи')
    authors = models.ManyToManyField(Author, verbose_name='Авторы')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        db_table = 'article'
