# coding=utf-8
from django.conf.urls import patterns, url

from bloger.views import IndexView, BlogDetailView


urlpatterns = patterns('',
    url(r'^index/$', IndexView.as_view(), name="index"),
    url(r'^article/detail/(?P<pk>\d+)/$', BlogDetailView.as_view(), name="article-detail"),
)