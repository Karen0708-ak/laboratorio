# Configuracion de rutas especificas de la app empresas
from django.urls import path
from . import views

urlpatterns=[
    path('iniciovi',views.inicio,name='iniciovi'),
    path('nuevoVinedo',views.nuevoVinedo),
    path('guardarVinedo',views.guardarVinedo),
    #path('eliminarVinedo/<id>',views.eliminarVinedo),
    #path('editarVinedo/<id>',views.editarVinedo),
    #path('procesarEdicionVinedo',views.procesarEdicionVinedo),
]