from django.contrib.auth.models import User, Group
from web.models import Payments, PaymentsTranscript
from rest_framework import serializers



class PaymentsTranscriptSerializer(serializers.ModelSerializer):
    class Meta:
        model =PaymentsTranscript
        fields = '__all__'

class PaymentsSerializer(serializers.ModelSerializer):
    #payments_transcript = PaymentsTranscriptSerializer(many=True)
    payment = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
     )
    author = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='username'
     )
    class Meta:
        model = Payments
        fields = '__all__'