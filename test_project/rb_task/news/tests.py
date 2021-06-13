from django.test import TestCase
from news.models import Author, Article


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(name='Bob')

    def test_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Имя')

    def test_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('name').max_length
        self.assertEquals(max_length, 20)

    def test_name_null_false(self):
        author = Author.objects.get(id=1)
        null = author._meta.get_field('name').null
        self.assertEquals(null, False)


class ArticleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        article = Article.objects.create(title='Bob', text='bobbob')
        author = Author.objects.create(name='Bob Bob')
        article.save()
        article.authors.add(author)

    def test_title_label(self):
        article = Article.objects.get(id=1)
        field_label = article._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Заголовок')

    def test_text_label(self):
        article = Article.objects.get(id=1)
        field_label = article._meta.get_field('text').verbose_name
        self.assertEquals(field_label, 'Текст статьи')

    def test_authors_label(self):
        article = Article.objects.get(id=1)
        field_label = article._meta.get_field('authors').verbose_name
        self.assertEquals(field_label, 'Авторы')

    def test_title_max_length(self):
        article = Article.objects.get(id=1)
        max_length = article._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)

    def test_text_max_length(self):
        article = Article.objects.get(id=1)
        max_length = article._meta.get_field('text').max_length
        self.assertEquals(max_length, 2000)

    def test_title_text_null_false(self):
        article = Article.objects.get(id=1)
        null_title = article._meta.get_field('title').null
        null_text = article._meta.get_field('text').null
        self.assertEquals(null_title, False)
        self.assertEquals(null_text, False)
