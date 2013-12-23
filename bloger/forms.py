# -*- coding: utf-8 -*-
from django import forms
from data.models import BlogComment

from captcha.fields import CaptchaField


class CommentModelForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = BlogComment