from django.shortcuts import render, render_to_response
from authsys.forms import AuthForm
from authsys.models import UserSettings
from django.template.context_processors import csrf
from web.models import PaymentsType

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer

def index(request, form=None):
    if not form:
        form = AuthForm(auto_id=False)
    params = {}
    params.update(csrf(request))
    params['form'] = form
    params['range'] = range(3)
    params['user'] = request.user
    user_icon = ''
    try:
        user_settings = UserSettings.objects.get(user__id=request.user.id)
        user_icon = user_settings.icon.url
    except:
        pass
    params['user_icon'] = user_icon;
    params['payment_types'] = PaymentsType.objects.all()
    return render_to_response('web/index.html', params)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer