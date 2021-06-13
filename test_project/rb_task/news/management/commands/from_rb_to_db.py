import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
from multiprocessing import cpu_count
from django.db.utils import IntegrityError
from django.core.management import BaseCommand
from news.models import Author, Article


class Command(BaseCommand):
    help = u'Заполнение базы данными из сайта RB.ru'

    def handle(self, *args, **kwargs):
        url = 'https://rb.ru/news/'
        urls = []
        response = requests.get(url)
        Author.objects.all().distinct('first_name', 'second_name')
        soup = BeautifulSoup(response.text, features='html.parser')
        for link in soup.find_all("a", class_="news-item__title"):
            href = link.get('href')
            urls.append(url + href[6:])
        for url in urls:
            print('parsing: ' + url)
            response = requests.get(url)
            soup = BeautifulSoup(response.text, features='html.parser')
            div = soup.find_all("div", class_="article__introduction")
            for item in div:
                text = item.find("p")
                title = item.find('div', itemprop="headline")
                name = item.find('span', itemprop="name")

            full_name = name.text.strip()
            authors = Author.objects.create(name=full_name)
            articles = Article.objects.create(title=title.text.strip(),
                                              text=text.text.strip())
            articles.save()
            articles.authors.add(authors)
