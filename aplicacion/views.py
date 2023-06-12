from django.shortcuts import render

def inicio(request):
    return render(request, "aplicacion/index.html")

def notebook(request):
    return render(request, "aplicacion/index.html")

def aio(request):
    return render(request, "aplicacion/aio.html")

def desktop(request):
    return render(request, "aplicacion/index.html")

def celulares(request):
    return render(request, "aplicacion/index.html")

