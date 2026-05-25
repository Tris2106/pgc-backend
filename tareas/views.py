from rest_framework import viewsets
from .models import Tarea, Categoria, Recordatorio
from .serializers import (
    TareaSerializer,
    CategoriaSerializer,
    RecordatorioSerializer
)


class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class RecordatorioViewSet(viewsets.ModelViewSet):
    queryset = Recordatorio.objects.all()
    serializer_class = RecordatorioSerializer