# coding=utf-8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^blog/', include('bloger.urls')),
    url(r'^accounts/', include('accounts.urls')),
)
