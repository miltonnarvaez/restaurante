from rest_framework import serializers
from .models import Producto
from .models import Bodega
from .models import TipoProducto
from .models import TipoFactura
from .models import UnidadMedida
from .models import Proveedor
from .models import Cliente
from .models import EstadoFactura
from .models import Entrada
from .models import FacturaEntrada
from .models import Salida
from .models import FacturaSalida
from .models import ReportePerdida 


class ProductoSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Producto
        fields = '__all__'
        read_only_fields = ('fecha_creacion',) 


class BodegaSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Bodega
        fields = '__all__'
        read_only_fields = ('fecha_creacion',)


class TipoProductoSerializer(serializers.ModelSerializer):  
    class Meta:
        model = TipoProducto
        fields = '__all__'
        read_only_fields = ('fecha_creacion',)


class TipoFacturaSerializer(serializers.ModelSerializer):  
    class Meta:
        model = TipoFactura
        fields = '__all__'
        read_only_fields = ('fecha_creacion',)


class UnidadMedidaSerializer(serializers.ModelSerializer):  
    class Meta:
        model = UnidadMedida
        fields = '__all__'
        read_only_fields = ('fecha_creacion',)


class ProveedorSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Proveedor
        fields = '__all__'
        read_only_fields = ('fecha_creacion',)


class ClienteSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Cliente
        fields = '__all__'
        read_only_fields = ('fecha_creacion',)


class EstadoFacturaSerializer(serializers.ModelSerializer):  
    class Meta:
        model = EstadoFactura
        fields = '__all__'
        read_only_fields = ('fecha_creacion',)


class EntradaSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Entrada
        fields = '__all__'
        read_only_fields = ('fecha_creacion',)


class FacturaEntradaSerializer(serializers.ModelSerializer):  
    class Meta:
        model = FacturaEntrada
        fields = '__all__'
        read_only_fields = ('fecha_creacion',)


class SalidaSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Salida
        fields = '__all__'
        read_only_fields = ('fecha_creacion',)


class FacturaSalidaSerializer(serializers.ModelSerializer):  
    class Meta:
        model = FacturaSalida
        fields = '__all__'
        read_only_fields = ('fecha_creacion',)


class ReportePerdidaSerializer(serializers.ModelSerializer):  
    class Meta:
        model = ReportePerdida
        fields = '__all__'
        read_only_fields = ('fecha_creacion',)