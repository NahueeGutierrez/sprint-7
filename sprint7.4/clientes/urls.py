from django.urls import path
from .views import buscar_cliente, ver_informacion_cliente

urlpatterns = [
    path('', buscar_cliente, name='buscar_cliente'),
]
