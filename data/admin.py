# -*- coding: utf-8 -*-
from django.contrib import admin
from data.models import BlogArticle


class BlogArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'count', 'createtime', 'updatetime')
    search_fields = ('title', )

admin.site.register(BlogArticle, BlogArticleAdmin)

