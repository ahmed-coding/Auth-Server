from rest_framework import serializers
from .models import Clint_sys


class ClintValditeSerializer(serializers.Serializer):
    username = serializers.CharField()
    code = serializers.CharField()


class ClintSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clint_sys
        fields = '__all__'
