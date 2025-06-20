from producto.models import Producto
from producto.models import Bodega
from producto.models import TipoProducto
from producto.models import TipoFactura
from producto.models import UnidadMedida
from producto.models import Proveedor
from producto.models import Cliente
from producto.models import EstadoFactura
from producto.models import Entrada
from producto.models import FacturaEntrada
from producto.models import Salida
from producto.models import FacturaSalida
from producto.models import ReportePerdida

from rest_framework import viewsets, permissions
from producto.serializers import ProductoSerializer
from producto.serializers import BodegaSerializer
from producto.serializers import TipoProductoSerializer
from producto.serializers import TipoFacturaSerializer
from producto.serializers import UnidadMedidaSerializer
from producto.serializers import ProveedorSerializer
from producto.serializers import ClienteSerializer
from producto.serializers import EstadoFacturaSerializer
from producto.serializers import EntradaSerializer
from producto.serializers import FacturaEntradaSerializer
from producto.serializers import SalidaSerializer
from producto.serializers import FacturaSalidaSerializer
from producto.serializers import ReportePerdidaSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tipo_producto']

class BodegaViewSet(viewsets.ModelViewSet):
    queryset = Bodega.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = BodegaSerializer

class TipoProductoViewSet(viewsets.ModelViewSet):
    queryset = TipoProducto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TipoProductoSerializer

class TipoFacturaViewSet(viewsets.ModelViewSet):
    queryset = TipoFactura.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TipoFacturaSerializer


class UnidadMedidaViewSet(viewsets.ModelViewSet):
    queryset = UnidadMedida.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UnidadMedidaSerializer


class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProveedorSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClienteSerializer


class EstadoFacturaViewSet(viewsets.ModelViewSet):
    queryset = EstadoFactura.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EstadoFacturaSerializer


class EstadoFacturaViewSet(viewsets.ModelViewSet):
    queryset = EstadoFactura.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EstadoFacturaSerializer


class EntradaViewSet(viewsets.ModelViewSet):
    queryset = Entrada.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EntradaSerializer


class FacturaEntradaViewSet(viewsets.ModelViewSet):
    queryset = FacturaEntrada.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FacturaEntradaSerializer


class SalidaViewSet(viewsets.ModelViewSet):
    queryset = Salida.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SalidaSerializer


class FacturaSalidaViewSet(viewsets.ModelViewSet):
    queryset = FacturaSalida.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FacturaSalidaSerializer


class ReportePerdidaViewSet(viewsets.ModelViewSet):
    queryset = ReportePerdida.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ReportePerdidaSerializer
