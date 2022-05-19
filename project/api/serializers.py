from dataclasses import fields
from rest_framework import serializers
from base.models import take

class takeSerializer(serializers.ModelSerializer):
    class Meta:
        model = take
        fields = '__all__'