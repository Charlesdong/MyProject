# coding=utf-8
from django.views.generic import TemplateView, DetailView
from data.models import BlogArticle


class IndexView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        return context


class BlogDetailView(DetailView):

    model = BlogArticle
    template_name = "page.html"

    def get_object(self, queryset=None):
        obj = super(BlogDetailView, self).get_object(queryset)
        obj.count += 1
        obj.save()
        return obj