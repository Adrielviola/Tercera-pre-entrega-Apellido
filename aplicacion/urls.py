from django.urls import path
from .views import saludo, dia, segundo, nombre, template

urlpatterns = [

    path('saludo/', saludo),
    path('dia/', dia),
    path('segundo/', segundo),
    path('nombre/<nombre>', nombre),
    path('template/', template),
    
]

