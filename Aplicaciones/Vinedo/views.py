#importando el modelo cargo
from .models import Vinedo
from django.shortcuts import render, redirect
from django.contrib import messages
def inicio(request):
    listadoVinedo=Vinedo.objects.all()
    return render(request,"iniciovi.html",{'vinedo':listadoVinedo})

def nuevoVinedo(request):
    return render(request,"nuevoVinedo.html")
#Almacenando los datos de cargo en la Bdd
def guardarVinedo(request):
    ubicacion = request.POST["ubicacion"]
    hectareas = request.POST["hectareas"]
    variedad_uva = request.POST["variedad_uva"]
    anio_plantacion = request.POST["anio_plantacion"]
    nuevoVinedo=Vinedo.objects.create(
            ubicacion=ubicacion,
            hectareas=hectareas,
            variedad_uva=variedad_uva,
            anio_plantacion = anio_plantacion,
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