from django.shortcuts import render

def inicio(request):
    return render(request, "aplicacion/inicio.html")

def notebook(request):
    return render(request, "aplicacion/notebook.html")

def aio(request):
    return render(request, "aplicacion/aio.html")

def desktop(request):
    return render(request, "aplicacion/desktop.html")

def celulares(request):
    return render(request, "aplicacion/celulares.html")

