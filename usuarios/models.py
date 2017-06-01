#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from django.db import models
from django.contrib.auth.models import User
from parametrizacion.models import Profesiones

class Usuarios(models.Model):
    nombres = models.CharField(max_length=70, null=False, blank=False)
    edad = models.CharField(max_length=2, null=False, blank=False)
    correo = models.CharField(max_length=50, null=False, blank=False)
    experiencia_anos = models.CharField(max_length=2, null=False, blank=False)
    experiencia_horas = models.CharField(max_length=8, null=False, blank=False)
    profesion = models.ForeignKey(Profesiones, null=True ,blank=False)
    certificado = models.TextField(null=False, blank=True)
    instruccion = models.CharField(max_length=50, null=False, blank=False)
    ciudad = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.nombres

    class Meta:
        verbose_name_plural = 'Crear Usuarios'
