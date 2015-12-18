# -*- coding: utf-8 -*-
__author__ = 'boris'

from django import forms
from django.contrib.auth import authenticate
from authsys.models import UserSettings

class AuthForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs = {'placeholder':'Логин'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs = {'placeholder':'Пароль'}))

    def clean(self):
        cleaned_data = super(AuthForm, self).clean()
        if not self.errors:
            user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
            if user is None:
                print('Имя пользователя и пароль не подходят')
                raise forms.ValidationError('Имя пользователя и пароль не подходят')
            self.user = user
        return cleaned_data

    def get_user(self):
        return self.user or None

class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = UserSettings
        fields = '__all__'

