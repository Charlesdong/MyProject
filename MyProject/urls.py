# coding=utf-8
from django.conf.urls import patterns, include, url
from bloger.views import BlogListView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^grappelli/',include('grappelli.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('bloger.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^$', BlogListView.as_view(), name="index"),
)