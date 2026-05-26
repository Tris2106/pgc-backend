from django.db import models
from usuarios.models import Usuario


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Tarea(models.Model):
    titulo = models.CharField(max_length=100)

    descripcion = models.TextField()

    fecha_entrega = models.DateField()

    prioridad = models.CharField(max_length=20)

    estado = models.CharField(
        max_length=20,
        default='Pendiente'
    )

    progreso = models.IntegerField(default=0)

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    
    def __str__(self):
        return self.titulo


class Recordatorio(models.Model):
    fecha_hora = models.DateTimeField()
    mensaje = models.TextField()
    activo = models.BooleanField(default=True)

    tarea = models.ForeignKey(
        Tarea,
        on_delete=models.CASCADE
    )