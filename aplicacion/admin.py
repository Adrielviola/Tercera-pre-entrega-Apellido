from django.contrib import admin
from .models import notebook, aio, desktop, celulares


@admin.register(aio)
class aioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido','marca','modelo','serie']
    search_fields = ('nombre', 'apellido','marca','modelo','serie',)
    ordering =  ('nombre', 'apellido','marca','modelo','serie',)
    List_editable = ['nombre', 'apellido','marca','modelo','serie']

@admin.register(notebook)
class notebookAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido','marca','modelo','serie']
    search_fields = ('nombre', 'apellido','marca','modelo','serie',)
    ordering = ('nombre', 'apellido','marca','modelo','serie',)
    List_editable = ['nombre', 'apellido','marca','modelo','serie']

@admin.register(desktop)
class desktopAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido','marca','modelo','serie']
    search_fields = ('nombre', 'apellido','marca','modelo','serie',)
    ordering = ('nombre', 'apellido','marca','modelo','serie',)
    List_editable = ['nombre', 'apellido','marca','modelo','serie']

@admin.register(celulares)
class celularesAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido','marca','modelo','imei']
    search_fields = ('nombre', 'apellido','marca','modelo','imei',)
    ordering = ('nombre', 'apellido','marca','modelo','imei',)
    List_editable = ['nombre', 'apellido','marca','modelo','imei']

# Register your models here.
