from django.contrib import admin
from parametrizacion.models import *

@admin.register(Profesiones)
class ProfesionesAdmin(admin.ModelAdmin):
    pass
