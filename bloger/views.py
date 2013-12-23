# coding=utf-8
from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView, DetailView, ListView, CreateView
from bloger.forms import CommentModelForm
from bloger.renders import JSONResponseMixin
from data.models import BlogArticle


class IndexView(TemplateView):
    
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        return context


class BlogDetailView(DetailView):

    model = BlogArticle

    def get_object(self, queryset=None):
        obj = super(BlogDetailView, self).get_object(queryset)
        obj.count += 1
        obj.save()
        return obj


class BlogListView(ListView):

    model = BlogArticle
    paginate_by = 10


class BlogCommentView(JSONResponseMixin, CreateView):

    form_class = CommentModelForm

    def form_invalid(self, form):
        if self.request.is_ajax():
            to_json_responce = dict()
            to_json_responce['status'] = 0
            to_json_responce['form_errors'] = form.errors

            to_json_responce['new_cptch_key'] = CaptchaStore.generate_key()
            to_json_responce['new_cptch_image'] = captcha_image_url(to_json_responce['new_cptch_key'])

            return self.render_to_response(to_json_responce)

    def form_valid(self, form):
        form.save()
        if self.request.is_ajax():
            to_json_responce = dict()
            to_json_responce['status'] = 1

            to_json_responce['new_cptch_key'] = CaptchaStore.generate_key()
            to_json_responce['new_cptch_image'] = captcha_image_url(to_json_responce['new_cptch_key'])

            return self.render_to_response(to_json_responce)

def test(request):
    if request.POST:
        form = CommentModelForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(request.path + '?ok')
    else:
        form = CommentModelForm()

    return render_to_response('home.html', dict(
        form=form
    ), context_instance=RequestContext(request))






