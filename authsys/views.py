from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from authsys.forms import AuthForm

def login(request):
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            print('err)')
            if form.get_user():
                print('err)')
                auth.login(request, form.get_user())
    return HttpResponseRedirect('/')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")