#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from django.db import models
from django.contrib.auth.models import User

def profesiones_directory_path(profesion, id):
    return "profesiones/"'{0}'.format(str(profesion)+".png")

class Profesiones(models.Model):
    profesion = models.CharField(max_length=50, null=False, blank=False)
    foto = models.ImageField(upload_to=profesiones_directory_path, blank=False)

    def __str__(self):
        return self.profesion

    class Meta:
        verbose_name_plural = 'Crear Profesiones'
