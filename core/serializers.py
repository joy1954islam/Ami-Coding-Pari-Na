from rest_framework import serializers
from .models import Khoj


class KhojSerializer(serializers.ModelSerializer):
    class Meta:
        model = Khoj
        fields = ['timestamp', 'input_values']
