from datetime import datetime as dt
from django.http import HttpResponse
from django.template import Context, Template
from django.template import loader

def saludo(request, saludo):
    return HttpResponse("Adriel")

def segundo(request):
    return HttpResponse("Ya lo conozco!!!")

def dia(request):
    dia=dt.now()
    texto =f"La fecha y hora es: <br> {dia}"
    return HttpResponse(texto)

def nombre(request, nombre):
    nombre = f"Mi nombre es: <br><br> {nombre}"
    return HttpResponse(nombre)
    

def template(request):
    #miHtml = open("./Proyecto1/planillas/index.html")

    listaDeNotas =[2,2,5,3,7,8,4,2,7,5,9]
    diccionario = {"nombre": "Adriel", "apellido": "viola", "notas": listaDeNotas}
    plantilla =loader.get_template('base.html')
    docu = plantilla.render(diccionario)
    return HttpResponse(docu)