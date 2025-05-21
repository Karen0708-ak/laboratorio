# Configuracion de rutas especificas de la app empresas
from django.urls import path
from . import views

urlpatterns=[
    path('inicioem',views.inicio,name='inicioem'),
]