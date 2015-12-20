from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from authsys.forms import AuthForm, UserSettingsForm, UserForm
from web.views import index
from django.core.context_processors import csrf
from .models import UserSettings
from django.contrib.auth.models import User
from django.template import RequestContext

def login(request):
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            print('err)')
            if form.get_user():
                print('err)')
                auth.login(request, form.get_user())
                return HttpResponseRedirect("/")
    return index(request, form = form)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

def user_settings(request, settigs_form=None, user_form=None):
    params = {}
    params.update(csrf(request))
    if not settigs_form:
        data = UserSettings.objects.filter(user__id = request.user.id).values()
        if len(data)==0:
            settigs_form= UserSettingsForm()
        else:
            settigs_form= UserSettingsForm(initial=data[0], files=data[0])
    if not user_form:
        data = User.objects.filter(id = request.user.id).values()
        user_form= UserForm(initial=data[0])
    params['settigs_form'] = settigs_form
    params['user_form'] = user_form
    return render_to_response('authsys/user_settings.html', params)

def add_user_settings(request):
    if request.method == 'POST':
        settigs_form = UserSettingsForm(request.POST, request.FILES)
        user_form = UserForm(request.POST, request.FILES)
        if settigs_form.is_valid() and user_form.is_valid():
            settigs_form.save()
            user_form.save()
            return HttpResponseRedirect("/")
        params={}
        params['settigs_form'] = UserSettingsForm()
        params['user_form'] = UserForm()
        return render(request, 'authsys/user_settings.html', params)
        #return user_settings(request, settigs_form=settigs_form, user_form=user_form)
