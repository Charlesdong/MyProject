# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from views import LoginView, RegisterAjaxView, LogoutView, LoginAjaXView, ComplateRegisterView


urlpatterns = patterns('',
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^login-ajax/', LoginAjaXView.as_view(), name='login-ajax'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
    url(r'^register-ajax/', RegisterAjaxView.as_view(), name='register-ajax'),
    url(r'^complate/register/', ComplateRegisterView.as_view(), name='complate-register'),
)

