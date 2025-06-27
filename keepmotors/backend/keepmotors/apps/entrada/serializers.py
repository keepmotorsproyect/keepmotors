from rest_framework import serializers
from .models import entrada  
class EntradaSerializer(serializers.ModelSerializer):  

    class Meta:
        model = entrada
        fields = '__all__'