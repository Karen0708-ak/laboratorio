# Configuracion de rutas especificas de la app empresas
from django.urls import path
from . import views

urlpatterns=[
    path('iniciomu',views.inicio,name='iniciomu'),
    path('nuevoMuestreo',views.nuevoMuestreo),
    path('guardarMuestreo',views.guardarMuestreo),
    #path('eliminarMuestreo/<id>',views.eliminarMuestreo),
    #path('editarMuestreo/<id>',views.editarMuestreo),
    #path('procesarEdicionMuestreo',views.procesarEdicionMuestreo),
]