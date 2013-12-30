# -*- coding: utf-8 -*-
from data.models import BlogClassification, BlogArticle


def get_blog_classify(request):
    classify_list = BlogClassification.objects.all()
    return {"classify_list": classify_list}


def get_blog_rank(request):
    rank_list = BlogArticle.objects.all().order_by("-count")[:5]
    return {"rank_list": rank_list}