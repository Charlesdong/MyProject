# coding=utf-8
from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView, DetailView, ListView, CreateView
from bloger.renders import JSONResponseMixin
from data.models import BlogArticle


class IndexView(TemplateView):
    
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        return context


class BlogDetailView(DetailView):

    model = BlogArticle


class BlogListView(ListView):

    model = BlogArticle
    paginate_by = 10
    context_object_name = 'object_list'

    def get_queryset(self):
        classfy_id = self.request.GET.get('classfy_id', None)

        queryset = self.model.objects.all()
        if classfy_id:
            queryset = queryset.filter(classify_id=classfy_id)
        return queryset


class BlogLifeListView(ListView):

    model = BlogArticle
    paginate_by = 10
    context_object_name = 'object_list'

    def get_queryset(self):
        queryset = self.model.objects.all()
        if classfy_id:
            queryset = queryset.filter(classify_id=classfy_id)
        return queryset