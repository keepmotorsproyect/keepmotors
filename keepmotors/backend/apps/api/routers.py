from rest_framework.routers import DefaultRouter

from ..entrada.views import entradaViewset
from ..espacios.views import EspacioViewSet
from ..login.views import loginViewset
from ..membresia.views import membresiaViewset
from ..salida.views import salidaViewset
from ..tarifas.views import tarifaViewset
from ..registro.views import registroViewset

router = DefaultRouter()

router.register(r'entrada', entradaViewset, basename='entrada')
router.register(r'espacios', EspacioViewSet, basename='espacios')
router.register(r'login', loginViewset, basename='login')
router.register(r'membresia', membresiaViewset, basename='membresia')
router.register(r'salida', salidaViewset, basename='salida')
router.register(r'tarifas', tarifaViewset, basename='tarifas')
router.register(r'registro', registroViewset, basename='registro')

urlpatterns = router.urls