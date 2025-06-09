from rest_framework import routers
from .api import ProductoViewSet
from .api import BodegaViewSet
from .api import TipoProductoViewSet
from .api import TipoFacturaViewSet
from .api import UnidadMedidaViewSet
from .api import ProveedorViewSet
from .api import ClienteViewSet
from .api import EstadoFacturaViewSet
from .api import EntradaViewSet
from .api import FacturaEntradaViewSet
from .api import SalidaViewSet
from .api import FacturaSalidaViewSet
from .api import ReportePerdidaViewSet     

router=  routers.DefaultRouter()

router.register('api/productos', ProductoViewSet, 'productos')
urlpatterns = router.urls

router.register('api/bodegas', BodegaViewSet, 'bodegas')
urlpatterns = router.urls

router.register('api/TipoProductos', TipoProductoViewSet, 'TipoProductos')
urlpatterns = router.urls

router.register('api/TipoFactura', TipoFacturaViewSet, 'TipoFactura')
urlpatterns = router.urls

router.register('api/UnidadMedida', UnidadMedidaViewSet, 'UnidadMedida')
urlpatterns = router.urls

router.register('api/Proveedor', ProveedorViewSet, 'Proveedor')
urlpatterns = router.urls

router.register('api/Cliente', ClienteViewSet, 'Cliente')
urlpatterns = router.urls

router.register('api/EstadoFactura', EstadoFacturaViewSet, 'EstadoFactura')
urlpatterns = router.urls

router.register('api/Entrada', EntradaViewSet, 'Entrada')
urlpatterns = router.urls

router.register('api/FacturaEntrada', FacturaEntradaViewSet, 'FacturaEntrada')
urlpatterns = router.urls

router.register('api/Salida', SalidaViewSet, 'Salida')
urlpatterns = router.urls

router.register('api/FacturaSalida', FacturaSalidaViewSet, 'FacturaSalida')
urlpatterns = router.urls

router.register('api/ReportePerdida', ReportePerdidaViewSet, 'ReportePerdida')
urlpatterns = router.urls