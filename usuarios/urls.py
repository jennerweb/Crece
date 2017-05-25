from django.conf import settings
from django.contrib import admin
from django.conf.urls import url,include
from django.conf.urls.static import static
from . import views

urlpatterns = [
   url('^$', views.index, name = 'index'),
   url('^saveUser$', views.guardarUsuario, name = 'guardarUsuario'),
   url('^experiencia/(?P<id>\d+)$', views.Experiencia, name = 'Experiencia' ),
   url('^certificadoPNG$', views.certificadoPNG, name = 'certificadoPNG'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
