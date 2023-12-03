from django.urls import path
from . import views  

urlpatterns = [
    path('', views.prestamos, name='prestamos'),
    path('respuesta', views.respuesta, name='respuesta'),
    path('pagina_de_exito', views.pagina_de_exito, name='pagina_de_exito')
    
]
