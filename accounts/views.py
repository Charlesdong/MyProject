# coding=utf-8
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.views.generic import View, RedirectView
from django.views.generic import FormView

from bloger.renders import JSONResponseMixin
from .forms import LoginForm
from utils.tool import send_html_mail


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


#class RegisterAjaxView(CreateView):
#
#    form_class = RegisterForm
#    template_name = 'register.html'
#    success_url = '/'
#    error_msg = ''
#
#    def form_valid(self, form):
#        username = form.cleaned_data['username']
#        password = form.cleaned_data['password']
#        email = form.cleaned_data['email']
#
#        if User.objects.filter(Q(username=username) | Q(email=email)).exists():
#            self.error_msg = 'username or email already exist!'
#            return self.form_invalid(form)
#        user = User.objects.create_user(username, email, password)
#        user.is_active = False
#        user.save()
#        return HttpResponseRedirect(self.get_success_url())
#
#    def form_invalid(self, form):
#        context = self.get_context_data(form=form)
#        context['error_msg'] = self.error_msg
#        return self.render_to_response(context)

class RegisterAjaxView(JSONResponseMixin, View):

    def post(self, request, *args, **kwargs):
        data = request.POST.copy()
        if User.objects.filter(Q(username=data["username"]) | Q(email=data["email"])).exists():
            return self.render_to_response({"result": "error01"})  # 用户名邮箱已存在
        if data['password'] != data['repassword']:
            return self.render_to_response({"result": "error02"})  # 两次密码不一致
        user = User.objects.create_user(data["username"], data["email"], data["password"])
        user.is_active = False
        user.save()
        sessionid = request.COOKIE.get('sessionid', '')
        send_html_mail(u'完成注册', { "id": user.id, "sessionid": sessionid }, user.email)


class ComplateRegisterView(View):

    def get(self, request, *args, **kwargs):
        user_id = request.GET.get("cookid")
        try:
            user = User.objects.get(id=user_id)
            if not user.is_active:
                user.is_active = True
                user.save()
                return HttpResponseRedirect(reverse('index'))
        except Exception:
            pass
        return  # 错误页



class ResetpasswordView(RedirectView):
    pass












