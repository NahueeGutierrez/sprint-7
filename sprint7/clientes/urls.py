from django.urls import path
from . import views  # Asegúrate de importar el módulo views

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes')
    # Agrega más rutas según sea necesario
]
