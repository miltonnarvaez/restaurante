from django.contrib import admin

from .models import Producto

@admin.register(Producto)

class Producto(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'fecha_creado', 'activo')
    


