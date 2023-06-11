from django.contrib import admin
from .models import notebook, aio, desktop, celulares

admin.site.register(notebook)
admin.site.register(aio)
admin.site.register(desktop)
admin.site.register(celulares)
# Register your models here.
