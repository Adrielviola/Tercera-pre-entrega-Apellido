#from datetime import datetime as dt
#from django.http import HttpResponse
#from django.template import Context, Template
#from django.template import loader
from django.shortcuts import render
#from aplicacion.models import notebook

def inicio(request):
    return render(request, "aplicacion/index.html")

def notebook(request):
    return render(request, "aplicacion/index.html")

def aio(request):
    return render(request, "aplicacion/index.html")

def desktop(request):
    return render(request, "aplicacion/index.html")

def celulares(request):
    return render(request, "aplicacion/index.html")

#def saludo(request):
 #   return HttpResponse("Adriel")

#def segundo(request):
 #   return HttpResponse("Ya lo conozco!!!")

#def dia(request):
 #   dia=dt.now()
  #  texto =f"La fecha y hora es: <br> {dia}"
   # return HttpResponse(texto)

#def nombre(request, nombre):
 #   nombre = f"Mi nombre es: <br><br> {nombre}"
  #  return HttpResponse(nombre)


#def template(request):
 #   #miHtml = open("./Proyecto1/planillas/index.html")

  #  listaDeNotas =[2,2,5,3,7,8,4,2,7,5,9]
   # diccionario = {"nombre": "Adriel", "apellido": "viola", "notas": listaDeNotas}
    ##plantilla =loader.get_template()
    #docu = plantilla.render(diccionario)
    #return HttpResponse(diccionario)

    #return render(request, "generales/base.html")

#def notebook(request, marca, modelo):
 #   computadora = notebook(marca=marca, modelo=int(modelo))
  #  computadora.save()
  #  documento = f"notebook: {notebook.marca}<br>modelo: {notebook.modelo}"

