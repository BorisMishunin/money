from django.shortcuts import render, redirect
from authsys.forms import AuthForm
from django.template.context_processors import csrf

# Create your views here.

def index(request, form=None):
    if not request.user.is_authenticated():
        return redirect('/')
    params = {}
    params.update(csrf(request))
    return render(request, 'fop/index.html', params)