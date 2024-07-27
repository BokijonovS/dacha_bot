from rest_framework import serializers

from .models import Dacha

class DachaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dacha
        fields = '__all__'

