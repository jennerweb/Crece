from django.contrib import admin
from usuarios.models import *

@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'edad', 'ciudad', 'correo')
