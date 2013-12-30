# coding=utf-8
from django.conf.urls import patterns, url

from bloger.views import BlogDetailView


urlpatterns = patterns('',
    #url(r'^$', BlogListView.as_view(), name="index"),
   # url(r'^article/list/$', BlogListView.as_view(), name="article-list"),
    url(r'^article/detail/(?P<pk>\d+)/$', BlogDetailView.as_view(), name="article-detail"),
)
