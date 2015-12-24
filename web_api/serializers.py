from django.contrib.auth.models import User, Group
from web.models import Payments
from rest_framework import serializers

class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'

