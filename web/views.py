from django.shortcuts import render, render_to_response
from authsys.forms import AuthForm
from authsys.models import UserSettings
from django.template.context_processors import csrf

def index(request, form=None):
    if not form:
        form = AuthForm(auto_id=False)
    params = {}
    params.update(csrf(request))
    params['form'] = form
    params['user'] = request.user
    user_icon = ''
    try:
        user_settings = UserSettings.objects.get(user__id=request.user.id)
        user_icon = user_settings.icon.url
    except:
        pass
    params['user_icon'] = user_icon;
    return render_to_response('web/index.html', params)