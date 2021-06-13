from django.conf.urls import url
from django.urls import path, reverse
from .views import *

urlpatterns = [
    url(r"^authors$", AuthorList.as_view(), name="authors"),
    url(r"^article_create$", ArticleFormView.as_view(), name="article_create"),
    url(r"^articles$", ArticleList.as_view(), name="articles"),
    url(r"authors/detail/(?P<pk>\d+)", AuthorDetail.as_view(), name="author"),
    url(r"articles/detail/(?P<pk>\d+)", ArticleDetail.as_view(), name="article"),
    url(r"", ArticleList.as_view(), name="base"),
]