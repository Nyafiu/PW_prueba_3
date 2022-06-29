from django.shortcuts import render
from django.http import HttpResponse
from vacunatorio.models import Informacion
# Create your views here.

def index(request):
    return render(request,"index.html")

def ingresar(request):
    return render(request,"ingresar.html")

def listar(request):
    return render(request,"listar.html")

def buscador(request):
    return render(request,"buscador_vacunados.html")

def ingresar_informacion(request):
    nombre_aux = request.GET["txt_nombre"]
    paterno_aux = request.GET["txt_appaterno"]
    materno_aux = request.GET["txt_apmaterno"]
    rut_aux = request.GET["txt_rut"]
    edad_aux = request.GET["txt_edad"]
    nombre_vacuna_aux = request.GET["txt_vacuna_nombre"]
    fecha = request.GET["fecha"]
    if len(nombre_aux)>0 and len(materno_aux)>0 and len(paterno_aux)>0 and len(rut_aux)>0 and len(edad_aux)>0 and len(nombre_vacuna_aux)>0 and len(fecha)>0:
        pro = Informacion(nombre=nombre_aux, apparteno=paterno_aux, apmaterno=materno_aux ,rut=rut_aux, edad=edad_aux, nombre_vacuna=nombre_vacuna_aux, fecha=fecha)
        pro.save()
        mensaje="<br><h2>Información ingresada.</h2>"
    else:
        mensaje="<br><h2>Debe ingresar la información.</h2>"
    return HttpResponse(mensaje+"<h4><a href='/index/'>Volver al inicio</a></h4>")

def listar_informacion(request):
    datos = Informacion.objects.all()
    return render(request,"listar.html",{'informacion':datos})


def buscar(request):
    if request.GET["txt_rut"]:
        persona = request.GET["txt_rut"]
        informacion = Informacion.objects.filter(rut__icontains=persona)
        return render(request,"buscador.html",{"informacion":informacion,"query":persona})
    else:
<<<<<<< HEAD
        mensaje = "<br><h2>Debe ingresar un rut válido...</h2>"
        return HttpResponse(mensaje+"<h4><a href='/index/'>Volver al inicio</a></h4>")
=======
        mensaje = "<h1>Debe ingresar un rut valido...</h1>"
        return HttpResponse(mensaje+"<br><h1><a href='/index/'>Volver al inicio</a></h1>")
>>>>>>> 88a80ffe33cdc3d692cc7e57d48e488d23cfc3a4
