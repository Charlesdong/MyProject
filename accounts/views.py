# coding=utf-8
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.template import loader
from django.views.generic import TemplateView, CreateView, View, UpdateView, RedirectView
from django.views.generic import FormView

from MyProject.settings import EMAIL_FROM_EMAIL
from bloger.renders import JSONResponseMixin
from .forms import LoginForm, RegisterForm


class LoginView(FormView):

    form_class = LoginForm
    success_url = "/"
    template_name = "index.html"

    def form_valid(self, form):
        username = form.cleaned_data['email']
        password = form.cleaned_data['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(self.get_success_url())
        else:
            context = self.get_context_data(form=form)
            return self.render_to_response(context)


class LoginAjaXView(JSONResponseMixin, View):

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(self.request, user)
                return self.render_to_response({"result": "success"})
        return self.render_to_response({"result": "fail"})


class LogoutView(RedirectView):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


def send_html_mail(subject, params, to_email):
    template_path = 'mailtemplate.html'

    html_content = loader.render_to_string(
        template_path,  # 需要渲染的html模板
        {
            'params': params  # 参数
        }
    )
    msg = send_mail(subject, html_content, EMAIL_FROM_EMAIL, to_email)
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()


class RegisterView(CreateView):

    form_class = RegisterForm
    template_name = 'register.html'
    success_url = '/'
    error_msg = ''

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']

        if User.objects.filter(Q(username=username) | Q(email=email)).exists():
            self.error_msg = 'username or email already exist!'
            return self.form_invalid(form)
        user = User.objects.create_user(username, email, password)
        user.is_active = False
        user.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        context['error_msg'] = self.error_msg
        return self.render_to_response(context)


class ResetpasswordView(RedirectView):
    pass












