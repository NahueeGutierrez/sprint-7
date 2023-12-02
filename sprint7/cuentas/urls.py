# cuentas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.crear_cuenta, name='crear_cuenta'),
    path('pagina_de_exito/', views.pagina_de_exito, name='pagina_de_exito'),  # Agrega esta línea

]
