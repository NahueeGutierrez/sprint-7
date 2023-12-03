from django.shortcuts import render, get_object_or_404
from .models import Cliente
from .forms import BusquedaClienteForm

def ver_informacion_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, customer_id=cliente_id)
    return render(request, 'clientes/informacion_cliente.html', {'cliente': cliente})

def buscar_cliente(request):
    cliente = None

    if request.method == 'POST':
        form = BusquedaClienteForm(request.POST)
        if form.is_valid():
            cliente_id = form.cleaned_data['cliente_id']
            cliente = get_object_or_404(Cliente, customer_id=cliente_id)
    else:
        form = BusquedaClienteForm()

    return render(request, 'buscar_cliente.html', {'form': form, 'cliente': cliente})
