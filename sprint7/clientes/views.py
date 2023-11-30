from django.shortcuts import render
from .models import Cliente

def lista_clientes(request):
    clientes = Cliente.objects.all()
     # Agrega esta línea para imprimir los clientes en la consola
    context = {'clientes': clientes}
    return render(request, 'lista_clientes.html', context)
