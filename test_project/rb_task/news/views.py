from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, FormView, TemplateView
from .models import Author, Article
from .forms import ArticleForm


class AuthorList(TemplateView):
    template_name = "authors.html"

    def get_authors(self):
        return Author.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AuthorList, self).get_context_data(**kwargs)
        lines = self.get_authors()
        paginator = Paginator(lines, 10)
        page = self.request.GET.get("page")
        try:
            show_lines = paginator.page(page)
        except PageNotAnInteger:

            show_lines = paginator.page(1)
        except EmptyPage:
            show_lines = paginator.page(paginator.num_pages)
        context["lines"] = show_lines
        return context


class ArticleList(TemplateView):
    template_name = "articles.html"

    def get_articles(self):
        return Article.objects.get_queryset().order_by('id')

    def get_context_data(self, **kwargs):
        context = super(ArticleList, self).get_context_data(**kwargs)
        lines = self.get_articles()
        paginator = Paginator(lines, 10)
        page = self.request.GET.get("page")
        try:
            show_lines = paginator.page(page)
        except PageNotAnInteger:
            show_lines = paginator.page(1)
        except EmptyPage:
            show_lines = paginator.page(paginator.num_pages)
        context["lines"] = show_lines
        return context


class AuthorDetail(DetailView):
    template_name = "author.html"
    model = Author

    def get_context_data(self, **kwargs):
        context = super(AuthorDetail, self).get_context_data(**kwargs)
        context['author_detail'] = Author.objects.get(pk=self.kwargs.get('pk'))
        context['articles'] = Article.objects.filter(authors=context['author_detail'].id).select_related()
        return context


class ArticleDetail(DetailView):
    template_name = "article.html"
    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleDetail, self).get_context_data(**kwargs)
        context['article_detail'] = Article.objects.get(pk=self.kwargs.get('pk'))
        return context


class ArticleFormView(FormView):
    template_name = "article_form.html"
    form_class = ArticleForm
    success_url = 'articles'

    def form_valid(self, form):
        instance = form.save(commit=False)
        authors = form.cleaned_data.get('authors')
        instance.save()
        instance.authors.add(*authors)
        return super(ArticleFormView, self).form_valid(form)
