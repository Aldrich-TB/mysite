#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())


class FileForm(forms.Form):
    taskname = forms.CharField(max_length=30)
    filename = forms.FileField()


class ContactForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField(max_length=30)
    message = forms.CharField(max_length=300)
