from rest_framework import serializers
from .models import *


class registroSerializer(serializers.ModelSerializer):

    class Meta:
        model = registro
        fields = ('__all__')