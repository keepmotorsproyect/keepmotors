from rest_framework.routers import DefaultRouter

from ..entrada.views import *
from ..espacios.views import *
from ..login.views import *
from ..membresia.views import *
from ..salida.views import *
from ..tarifas.views import *
from ..registro.views import *
router= DefaultRouter()

router.register(r'entrada', entradaViewset, basename='entrada')
router.register(r'espacios', espaciosViewset, basename='espacios')
router.register(r'login', loginViewset, basename='login')
router.register(r'membresia', membresiaViewset, basename='membrasia')
router.register(r'salida', salidaViewset, basename='salida')
router.register(r'tarifas', tarifaViewset, basename='tarifas')
router.register(r'registro', registroViewset, basename='registro')
urlpatterns = router.urls