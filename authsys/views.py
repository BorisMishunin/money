from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from authsys.forms import AuthForm, UserSettingsForm
from web.views import index
from django.core.context_processors import csrf

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

def user_settings(request):
    params = {}
    params.update(csrf(request))
    params['form'] = UserSettingsForm()
    return render_to_response('authsys/user_settings.html', params)