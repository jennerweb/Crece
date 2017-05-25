#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponse,Http404
from django.shortcuts import render, render_to_response
from django.template.loader import render_to_string
from django.template import RequestContext
from django.db import transaction
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from usuarios.models import Usuarios
from parametrizacion.models import Profesiones
from crece.settings import URL
import xhtml2pdf.pisa as pisa
from StringIO import StringIO
import os

def index(request):
    profesiones = Profesiones.objects.all()
    return render(request, "index.html", {'profesiones': profesiones })


from django.core.mail import send_mail, EmailMultiAlternatives
from crece.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string
def guardarUsuario(request):
    if request.method == 'POST':
        u = Usuarios()
        u.nombres = request.POST['nombres']
        u.edad = request.POST['edad']
        u.correo = request.POST['correo']
        u.experiencia_anos = request.POST['experiencia']
        u.experiencia_horas = int(request.POST['experiencia']) * 8760
        u.profesion_id = request.POST['profesion']
        u.save()

        os.makedirs("media/usuarios/"+str(u.id))

        usuario = Usuarios.objects.get(id=u.id)
        asunto = "SUMALE VALOR A TU EXPERIENCIA"
        body = render_to_string('correo.html', { 'user': usuario})
        msg = EmailMultiAlternatives(asunto, body, EMAIL_HOST_USER, [ usuario.correo ] )
        msg.content_subtype = "html"
        msg.send()

        return HttpResponseRedirect('/experiencia/'+str(u.id))
    else:
        return HttpResponseRedirect('/')

def Experiencia(request, id):
    try:
        url = URL
        usuario = Usuarios.objects.get(id=id)
        profesion = Profesiones.objects.get(id=usuario.profesion_id)
        return render(request, "experiencia.html", {'usuario': usuario , 'profesion': profesion , 'url': url })
    except Usuarios.DoesNotExist:
        return HttpResponseRedirect('/')

import Image, io, base64
def certificadoPNG(request):
    if request.method == 'POST':
        id = request.POST['codigo_usuario']
        png_b64 = request.POST['imgB64']
        png_recovered = Image.open(io.BytesIO(base64.b64decode(png_b64.split(',')[1])))
        ruta = "media/usuarios/"+str(id)+"/experiencia.png"
        png_recovered.save(ruta)
        u = Usuarios.objects.get(id=id)
        u.certificado = ruta
        u.save()

        return HttpResponseRedirect('/experiencia/'+str(id))
    else:
        return HttpResponseRedirect('/')
