from django.shortcuts import render, redirect
from .models import *
from .forms import CrearPrestamoForm
from django.contrib.auth.decorators import login_required

@login_required
def prestamos(request):
    return render(request, 'formulario.html', {})

def respuesta(request):
    mensaje = None

    if request.method == 'POST':
        id_tipCliente = request.POST['id_tipCliente']

        try:
            tipo_cliente = Tiposclientes.objects.get(id_tipcliente=id_tipCliente)
            if tipo_cliente.id_tipcliente == 1:
                mensaje = f'Usted pertenece a la cuenta {tipo_cliente} por lo tanto tiene acceso a $100.000, le pedimos que se comunique a este numero 3517288475 para completar los requerimientos'
            elif tipo_cliente.id_tipcliente == 2:
                mensaje = f'Usted pertenece a la cuenta {tipo_cliente} por lo tanto tiene acceso a $300.000, le pedimos que se comunique a este numero 3557218270 para completar los requerimientos'
            elif tipo_cliente.id_tipcliente == 3:
                mensaje = f'Usted pertenece a la cuenta {tipo_cliente} por lo tanto tiene acceso a $500.000, le pedimos que se comunique a este numero 3587068210 para completar los requerimientos'
        except Tiposclientes.DoesNotExist or tipo_cliente.id_tipcliente not in [1, 2, 3]:
                mensaje = 'Este cliente no existe o no tiene un tipo de cliente registrado.'

        form = CrearPrestamoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina_de_exito')

    else:
        form = CrearPrestamoForm()
    
    return render(request, 'respuesta.html', {'mensaje': mensaje, 'form': form})

def pagina_de_exito(request):
    return render(request, 'pagina_de_exito.html')
