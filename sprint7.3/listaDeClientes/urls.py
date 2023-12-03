from django.urls import path
from .views import lista_cuentas_cliente

urlpatterns = [
    path('', lista_cuentas_cliente, name='lista_cuentas_cliente'),
]
