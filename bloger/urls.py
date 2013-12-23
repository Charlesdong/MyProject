# coding=utf-8
from django.conf.urls import patterns, url

from bloger.views import BlogDetailView, BlogCommentView, test


urlpatterns = patterns('',
    #url(r'^$', BlogListView.as_view(), name="index"),
   # url(r'^article/list/$', BlogListView.as_view(), name="article-list"),
    url(r'^article/detail/(?P<pk>\d+)/$', BlogDetailView.as_view(), name="article-detail"),
    url(r'^article/comment/$', BlogCommentView.as_view(), name="blog-comment"),
    url(r'^comment/test/$', test, name="test"),
)