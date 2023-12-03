"""
URL configuration for sprint7 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from ot  her_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from .views import *
=======
from cuentas.views import crear_cuenta  
from listaDeClientes.views import lista_cuentas_cliente



>>>>>>> 4703cdf24af51e283beff8fd39cca96d64c0c184



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',include('login.urls')),
    path('clientes/', include('clientes.urls')), 
<<<<<<< HEAD
    path('prestamos/',include('prestamos.urls')),
    path('cuentas/', include('cuentas.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
=======
    path('cuentas/', include('cuentas.urls')),
    path('listaDeClientes/', include('listaDeClientes.urls')), 
>>>>>>> 4703cdf24af51e283beff8fd39cca96d64c0c184
]   

    