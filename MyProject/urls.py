# coding=utf-8
from django.conf.urls import patterns, include, url
from bloger.views import BlogListView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^blog/', include('bloger.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^$', BlogListView.as_view(), name="index"),
)
