# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm


class LoginForm(forms.Form):
    email = forms.CharField(max_length=10)
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(ModelForm):
    repassword = forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = User
        fields = ('username', 'password', 'email',)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data['password']
        repassword = cleaned_data['repassword']

        if password != repassword:
            raise forms.ValidationError("password error!")
        return cleaned_data
