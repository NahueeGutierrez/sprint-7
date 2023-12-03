# cuentas/views.py
from django.shortcuts import render, redirect
from .forms import CrearCuentaForm

def crear_cuenta(request):
    if request.method == 'POST':
        form = CrearCuentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina_de_exito')
    else:
        form = CrearCuentaForm()

    return render(request, 'crear_cuenta.html', {'form': form})



def pagina_de_exito(request):
    return render(request, 'pagina_de_exito.html')