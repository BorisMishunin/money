
from rest_framework import viewsets
from web_api.serializers import PaymentsSerializer
from web.models import Payments

from django.http import HttpResponse

from rest_framework.parsers import JSONParser

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import generics


class PaymentList(generics.ListCreateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer


class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer