from django.urls import path
from .views import registro, user_login, user_logout

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]