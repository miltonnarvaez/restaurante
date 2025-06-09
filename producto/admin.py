from django.contrib import admin
from .models import Bodega, UnidadMedida, Proveedor, Cliente,Entrada , EstadoFactura, FacturaEntrada, Salida,FacturaSalida, TipoFactura, Producto,TipoProducto

@admin.register(TipoProducto)
class TipoProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    list_filter = ('nombre',)
    ordering = ('-nombre',)

@admin.register(TipoFactura)
class TipoFacturaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    list_filter = ('nombre',)
    ordering = ('-nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_producto', 'precio_compra', 'bodega')
    search_fields = ('nombre',)
    list_filter = ('tipo_producto',)
    ordering = ('-nombre',) 
    list_editable = ('precio_compra', 'bodega')
    list_display_links = ('nombre',)           

@admin.register(Bodega)
class BodegaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'altitud', 'latitud', 'longitud')
    search_fields = ('nombre',)
    list_filter = ('direccion',)
    ordering = ('-nombre',) 

@admin.register(UnidadMedida)
class UnidadMedidaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'sigla')
    search_fields = ('nombre',)
    list_filter = ('sigla',)
    ordering = ('-nombre',)

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'telefono', 'correo', 'cedula', 'direccion', 'estado', 'creado')
    search_fields = ('nombre', 'apellido')
    list_filter = ('estado',)
    ordering = ('-creado',) 

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('cedula','nombre', 'apellido', 'telefono', 'correo' , 'direccion', 'creado')
    search_fields = ('nombre', 'apellido')
    list_filter = ('creado',)
    ordering = ('-creado',)

@admin.register(EstadoFactura)
class EstadoFacturaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    list_filter = ('nombre',)
    ordering = ('-nombre',)     

@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    list_display = ('proveedor', 'descripcion', 'precio', 'fecha_entrada', 'creado', 'EstadoFactura','foto')
    search_fields = ('proveedor__nombre',)
    list_filter = ('fecha_entrada',)
    ordering = ('-fecha_entrada',)
    date_hierarchy = 'fecha_entrada'
    list_per_page = 10
    list_editable = ('precio', 'EstadoFactura')
    list_display_links = ('proveedor', 'descripcion')   


@admin.register(FacturaEntrada)
class FacturaEntradaAdmin(admin.ModelAdmin):
    list_display = ('entrada', 'cantidad', 'unidad_medida', 'subtotal')
   
    list_editable = ('cantidad', 'unidad_medida')

@admin.register(Salida)
class SalidaAdmin(admin.ModelAdmin):
    list_display = ('producto', 'unidad_medida', 'cantidad', 'lote', 'fecha_salida', 'cliente')
    search_fields = ('producto', 'cliente__nombre')
    list_filter = ('fecha_salida',)
    ordering = ('-fecha_salida',)  

@admin.register(FacturaSalida)
class FacturaSalidaAdmin(admin.ModelAdmin):
    list_display = ('salida', 'estado_factura','total_pagar')

"""
@admin.register(FacturaSalida)
class FacturaSalidaAdmin(admin.ModelAdmin):
    list_display = ('entrada', 'cantidad', 'unidad_medida', 'subtotal')
"""

""""
@admin.register(FacturaSalida)

class FacturaSalidaAdmin(admin.ModelAdmin):
    list_display = ('entrada', 'cantidad', 'unidad_medida', 'precio_unitario', 'total')
    search_fields = ('entrada__proveedor__nombre',)
    list_filter = ('entrada__fecha_entrada',)
    ordering = ('-entrada__fecha_entrada',)
    date_hierarchy = 'entrada__fecha_entrada'
    list_per_page = 10
    list_editable = ('cantidad', 'unidad_medida', 'precio_unitario')
    list_display_links = ('entrada',)
"""
          