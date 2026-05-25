from rest_framework import viewsets
from .models import Calendario
from .serializers import CalendarioSerializer


class CalendarioViewSet(viewsets.ModelViewSet):
    queryset = Calendario.objects.all()
    serializer_class = CalendarioSerializer