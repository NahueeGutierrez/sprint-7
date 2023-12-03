from django.shortcuts import render
from .models import Cliente
from cuentas.models import Cuenta  
from .forms import BusquedaClienteForm

def lista_cuentas_cliente(request):
    resultados = None
    cuentas_cliente = None

    if request.method == 'POST':
        form = BusquedaClienteForm(request.POST)    
        if form.is_valid():
            cliente_id = form.cleaned_data['cliente_id']
            resultados = Cliente.objects.filter(customer_id=cliente_id)
            cuentas_cliente = Cuenta.objects.filter(customer_id=cliente_id)
    else:
        form = BusquedaClienteForm()

    return render(request, 'lista_cuentas_cliente.html', {'form': form, 'resultados': resultados, 'cuentas_cliente': cuentas_cliente})
