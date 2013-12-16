# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from pagedown.widgets import AdminPagedownWidget
from data.models import BlogArticle, BlogComment, BlogClassification


class BlogArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'count', 'createtime', 'updatetime')
    search_fields = ('title', )
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }

class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('email',)


class BlogClassificationAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(BlogComment, BlogCommentAdmin)
admin.site.register(BlogClassification, BlogClassificationAdmin)
admin.site.register(BlogArticle, BlogArticleAdmin)

