# coding=utf-8
from django.contrib.comments import CommentForm
from django.views.generic import TemplateView, DetailView, View
from bloger.renders import JSONResponseMixin
from data.models import BlogArticle


class IndexView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        return context


class BlogDetailView(DetailView):

    model = BlogArticle
    template_name = "page.html"

    def get_object(self, queryset=None):
        obj = super(BlogDetailView, self).get_object(queryset)
        obj.count += 1
        obj.save()
        return obj


class CommentPostView(JSONResponseMixin, View):

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_obj = comment_form.save(commit=True)
            comment_obj.save()
            self.render_to_response({"result": "success"})
        else:
            self.render_to_response({"result": "fail"})