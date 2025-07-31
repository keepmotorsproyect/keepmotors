"""
URL configuration for keepmotors project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.login.views import *
from apps.entrada.views import *
from apps.espacios.views import *
from apps.membresia.views import *
from apps.registro.views import *
from apps.salida.views import *
from apps.tarifas.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.api.routers')),

    path('/', loginViewset.as_view(template_name='login/login.html'),
name='login'),

 path('entrada/', entradaViewset.as_view(template_name='entrada/entrada.html'),
name='entrada'),

 path('espacios/', EspacioViewSet.as_view(template_name='espacios/espacios.html'),
name='espacios'),

 path('membresia/', membresiaViewset.as_view(template_name='membresia/membresias.html'),
name='membresia'),

 path('registro/', registroViewset.as_view(template_name='registro/registro.html'),
name='espacios'),

 path('salida/', salidaViewset.as_view(template_name='salida/salida.html'),
name='salida'),

 path('tarifa/', tarifaViewset.as_view(template_name='tarifa/tarifas.html'),
name='espacios'),

]