from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    carrera = models.CharField(max_length=100)
    hobbys = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre