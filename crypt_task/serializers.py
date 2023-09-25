from rest_framework import serializers

from .models import CryptTaskModel


class CryptTaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = CryptTaskModel
        fields = ('encrypted_data',)


class CryptTaskGetSerializers(serializers.ModelSerializer):
    class Meta:
        model = CryptTaskModel
        fields = '__all__'



