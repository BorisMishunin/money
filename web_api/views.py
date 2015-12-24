
from rest_framework import viewsets
from web_api.serializers import PaymentsSerializer
from web.models import Payments

from django.http import HttpResponse

from rest_framework.parsers import JSONParser

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def payment_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        payments = Payments.objects.all()
        serializer = PaymentsSerializer(payments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PaymentsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def payment_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        payment = Payments.objects.get(pk=pk)
    except Payments.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PaymentsSerializer(payment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PaymentsSerializer(payment, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        payment.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)