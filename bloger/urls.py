# coding=utf-8
from django.conf.urls import patterns, url

from bloger.views import BlogDetailView, BlogCommentsView


urlpatterns = patterns('',
    #url(r'^$', BlogListView.as_view(), name="index"),
   # url(r'^article/list/$', BlogListView.as_view(), name="article-list"),
    url(r'^article/detail/(?P<pk>\d+)/$', BlogDetailView.as_view(), name="article-detail"),
    url(r'^article/comments/$', BlogCommentsView.as_view(), name="article-comments"),
    #url(r'^comments/post/$', comments_post, name="comments_post"),
)
