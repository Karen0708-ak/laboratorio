#importando el modelo cargo
from .models import Empleado
from django.shortcuts import render, redirect
#esta función es para renderizar el listado de cargos
def inicio(request):
    listadoEmpleado=Empleado.objects.all()
    return render(request,"inicioem.html",{'empleado':listadoEmpleado})