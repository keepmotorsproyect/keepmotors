from rest_framework import serializers
from .models import *


class membresiaSerializer(serializers.ModelSerializer):

    class Meta:
        model = membresia
        fields = ('__all__')