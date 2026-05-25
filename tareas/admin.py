from django.contrib import admin
from .models import Tarea, Categoria, Recordatorio

admin.site.register(Tarea)
admin.site.register(Categoria)
admin.site.register(Recordatorio)