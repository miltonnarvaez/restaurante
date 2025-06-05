from django.contrib import admin

from .models import Producto, TipoProducto

@admin.register(Producto)

class Producto(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'precio', 'activo', 'fecha_creado', 'fecha_vencimiento')	

@admin.register(TipoProducto)
class TipoProducto(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')

   
    


