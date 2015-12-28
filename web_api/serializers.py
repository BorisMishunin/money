from django.contrib.auth.models import User, Group
from web.models import Payments, PaymentsTranscript
from rest_framework import serializers



class PaymentsTranscriptSerializer(serializers.ModelSerializer):
    class Meta:
        model =PaymentsTranscript
        fields = '__all__'

class PaymentsSerializer(serializers.ModelSerializer):
    payments_transcript = PaymentsTranscriptSerializer(many=True)
    class Meta:
        model = Payments
        fields = '__all__'