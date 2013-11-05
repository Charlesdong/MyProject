# coding=utf-8
from django.conf.urls import patterns, url

from bloger.views import IndexView, BlogDetailView, CommentPostView


urlpatterns = patterns('',
    url(r'^index/$', IndexView.as_view(), name="index"),
    url(r'^article/detail/(?P<pk>\d+)/$', BlogDetailView.as_view(), name="article-detail"),
    url(r'^article/comment/post/$', CommentPostView.as_view(), name="comment-post"),
)