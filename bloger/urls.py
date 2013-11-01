# coding=utf-8
from django.conf.urls import patterns, url

from bloger.views import IndexView


urlpatterns = patterns('',
    url(r'^index/', IndexView.as_view(), name="index"),
)