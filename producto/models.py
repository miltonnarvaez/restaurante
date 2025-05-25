from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    activo = models.BooleanField(default=False)
    fecha_creado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha_creado']

    def __str__(self):
        return self.nombre

