from django.shortcuts import render, render_to_response
from authsys.forms import AuthForm
from django.template.context_processors import csrf

def index(request):
    form = AuthForm(auto_id=False)
    params = {}
    params.update(csrf(request))
    params['form'] = form
    return render_to_response('web/index.html', params)