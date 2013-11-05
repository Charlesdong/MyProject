# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from views import LoginView, RegisterView, LogoutView, LoginAjaXView


urlpatterns = patterns('',
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^login-ajax/', LoginAjaXView.as_view(), name='login-ajax'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
    url(r'^register/', RegisterView.as_view(), name='register'),
)

