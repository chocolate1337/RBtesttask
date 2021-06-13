from django.core.management import BaseCommand
from django.utils import lorem_ipsum
import random

from news.models import Author, Article


class Command(BaseCommand):
    help = u'Заполнение базы случайными данными'

    def handle(self, *args, **kwargs):
        random_name = lorem_ipsum.words(2, common=True)

        for _ in range(1, 21, 1):
            authors = Author.objects.create(name=random_name)
            authors.save()
        for _ in range(1, 31, 1):
            count_authors = random.randint(1, 4)
            count_title = random.randint(2, 7)
            articles = Article.objects.create(title=lorem_ipsum.words(count_title),
                                              text=lorem_ipsum.paragraphs(count=1))
            articles.save()
            for _ in range(count_authors):
                authors = Author.objects.random()
                articles.authors.add(authors)
