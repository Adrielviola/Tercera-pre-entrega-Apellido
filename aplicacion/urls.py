from django.urls import path
from aplicacion import views


urlpatterns=[

    #path('saludo/', saludo),
    #path('dia/', dia),
    #path('segundo/', segundo),
    #path('nombre/<nombre>', nombre),
    #path('template/', template),
    #path('',views.inicio, name="Inicio"),
    path('', views.inicio, name="Inicio"),
    path('notebook/', views.notebook, name="notebook"),
    path('aio/', views.aio, name="aio"),
    path('Desktop/', views.desktop, name="desktop"),
    path('celulares', views.celulares, name="celulares")
    ]

