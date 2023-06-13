from django.shortcuts import render
from .models import notebook

def index(request):
    return render(request, "aplicacion/index.html")

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

def login(request):
    return render(request, "aplicacion/login.html")

def inventarioFormulario(request):
    if request.method == 'POST':
        print(f"\n\n{request.POST}\n")
        NOTEBOOK = notebook(NOTEBOOK = request.POST['NOTEBOOK'], serie = request.POST['serie'])
        NOTEBOOK.save()
        return render(request, "generales/index.html")
    
    return render(request, "aplicacion/inventarioFormulario.html")
