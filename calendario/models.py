from django.db import models
from usuarios.models import Usuario


class Calendario(models.Model):
    titulo = models.CharField(max_length=100)
    fecha = models.DateField()
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE
    )