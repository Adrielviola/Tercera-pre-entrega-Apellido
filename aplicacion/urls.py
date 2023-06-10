
from django.contrib import admin
from django.urls import path
from .views import saludo,segundo,dia, nombre,template


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('dia/', dia),
    path('segundo/', segundo),
    path('nombre/', nombre),
    path('template/', template)
]

