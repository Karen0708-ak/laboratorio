#importando el modelo cargo
from .models import Muestreo
from .models import Vinedo
from .models import Empleado
from django.shortcuts import render, redirect
from django.contrib import messages
def inicio(request):
    listadoMuestreo=Muestreo.objects.all()
    return render(request,"iniciomu.html",{'muestreo':listadoMuestreo})

def nuevoMuestreo(request):
    rempleados=Empleado.objects.all()
    lvinedos=Vinedo.objects.all()
    return render(request,"nuevoMuestreo.html",{'empleados':rempleados,'vinedos':lvinedos})
#Almacenando los datos de cargo en la Bdd
def guardarVinedo(request):
    fecha = request.POST["fecha"]
    resulados = request.POST["resulados"]
    analistaid = request.POST["analista"]
    analista=Empleado.objects.get(id=analistaid)
    vinedoid = request.POST["vinedo"]
    vinedo=Vinedo.objects.get(id=vinedoid)
    nuevoMuestreo=Muestreo.objects.create(
            fecha=fecha,
            resulados=resulados,
            analista=analista,
            vinedo=vinedo,
        )
    #mensaje de confirmacion
    messages.success(request,"Viñedo guardado exitosamente")
    return redirect('iniciovi')
def eliminarVinedo(request,id):
    vinedoEliminar = Vinedo.objects.get(id=id)
    vinedoEliminar.delete()
    messages.success(request,"Viñedo ELIMINADO exitosamente")
    return redirect('iniciovi')

#editar
def editarVinedo(request,id):
    vinedoEditar=Vinedo.objects.get(id=id)
    return render(request,"editarVinedo.html",{'vinedoEditar':vinedoEditar})

def procesarEdicionVinedo(request):
    id=request.POST["id"]
    ubicacion = request.POST["ubicacion"]
    hectareas = request.POST["hectareas"].replace(',','.')
    variedad_uva = request.POST["variedad_uva"]
    anio_plantacion = request.POST["anio_plantacion"]
    vinedo=Vinedo.objects.get(id=id)
    vinedo.ubicacion=ubicacion
    vinedo.hectareas=hectareas
    vinedo.variedad_uva= variedad_uva
    vinedo.anio_plantacion= anio_plantacion
    vinedo.save()
    #mensaje de confirmacion
    messages.success(request,"Viñedo ACTUALIZADO exitosamente")
    return redirect('iniciovi')