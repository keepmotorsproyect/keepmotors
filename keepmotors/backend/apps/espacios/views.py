from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Espacio
from .serializers import EspacioSerializer

class EspacioViewSet(viewsets.ModelViewSet):
    queryset = Espacio.objects.all()
    serializer_class = EspacioSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'