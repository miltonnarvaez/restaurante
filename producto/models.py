from django.db import models

class Bodega(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(blank=True)
    altitud = models.CharField(blank=True)
    latitud = models.CharField(blank=True)
    longitud = models.CharField(blank=True)

    def __str__(self):
        return f"{self.nombre} {self.direccion}"
    
class TipoProducto(models.Model): 
    nombre = models.CharField(max_length=50)  # bultos, kilos, toneladas
    descripcion = models.CharField(max_length=128)

    def __str__(self): 
        return f"{self.nombre} {self.descripcion}"

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    tipo_producto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateField(auto_now=True) 

    def __str__(self):
        return f"{self.nombre} {self.tipo_producto} {self.bodega} {self.precio_compra} {self.precio_venta}"   

class TipoFactura(models.Model):
    nombre = models.CharField(max_length=50)  # bultos, kilos, toneladas
    descripcion = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.nombre} {self.descripcion}"


class UnidadMedida(models.Model):
    nombre = models.CharField(max_length=50)  # bultos, kilos, toneladas
    sigla = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.nombre} {self.sigla}"

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(blank=True)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(blank=True)
    cedula = models.CharField(max_length=20)
    direccion = models.CharField(blank=True)
    estado = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now= True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Cliente(models.Model):
    cedula = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(blank=True)  
    direccion = models.CharField(blank=True)
    creado = models.DateTimeField(auto_now= True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class EstadoFactura(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre}"
    

class Entrada(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='entradas/', blank=True)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_entrada = models.DateField()  
    creado = models.DateField(auto_now=True)
    EstadoFactura = models.ForeignKey(EstadoFactura, on_delete=models.CASCADE)
    TipoFactura = models.ForeignKey(TipoFactura, on_delete=models.CASCADE)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.proveedor} {self.precio} {self.EstadoFactura} {self.fecha_entrada}"
    
class FacturaEntrada(models.Model):
    entrada = models.ForeignKey(Entrada, on_delete=models.CASCADE)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    lote = models.CharField(blank=True)
    cantidad = models.CharField(max_length=100)
    subtotal = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.unidad_medida} {self.lote} {self.cantidad} {self.subtotal}"



class Salida(models.Model):
    producto = models.CharField(max_length=100)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    lote = models.CharField(max_length=100)
    fecha_salida = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

      
    def __str__(self):
        return f"{self.producto} {self.unidad_medida} {self.cantidad} {self.lote} {self.fecha_salida} {self.cliente}"

class FacturaSalida(models.Model):
    salida = models.ForeignKey(Salida, on_delete=models.CASCADE)
    estado_factura = models.CharField(max_length=50)
    total_pagar = models.DecimalField(max_digits=10, decimal_places=2)

class ReportePerdida(models.Model):
    entrada = models.ForeignKey(Entrada, on_delete=models.CASCADE)
    perdida_kilos = models.DecimalField(max_digits=10, decimal_places=2)