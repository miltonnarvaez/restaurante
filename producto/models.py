from django.db import models

class TipoProducto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-nombre']

    def __str__(self):
        return self.nombre
    

class Producto(models.Model):
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    activo = models.BooleanField(default=True)
    fecha_creado = models.DateTimeField(auto_now=True)
    fecha_vencimiento = models.DateTimeField(blank=True)

    class Meta:
        ordering = ['-fecha_creado']

    def __str__(self):
        return self.nombre

"""
dsadasda
"""