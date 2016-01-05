

from web_api.serializers import PaymentsSerializer, PaymentsTranscriptSerializer
from web.models import Payments, PaymentsTranscript
from rest_framework import generics
from .permissions import UserPermissions
from rest_framework import filters


class PaymentList(generics.ListCreateAPIView):
    def get_queryset(self):
        if self.request.user.is_authenticated():
            return Payments.objects.filter(author=self.request.user)
        else:
            return Payments.objects.none()

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