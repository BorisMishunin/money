

from web_api.serializers import PaymentsSerializer, PaymentsTranscriptSerializer
from web.models import Payments, PaymentsTranscript
from rest_framework import generics


class PaymentList(generics.ListCreateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer

class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer

class PaymentsTranscriptList(generics.ListCreateAPIView):
    queryset = PaymentsTranscript.objects.all()
    serializer_class = PaymentsTranscriptSerializer

class PaymentsTranscriptDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentsTranscript.objects.all()
    serializer_class = PaymentsTranscriptSerializer