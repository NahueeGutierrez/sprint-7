from django.shortcuts import render

def lista_clientes(request):
    # Aquí puedes realizar operaciones necesarias y devolver una respuesta
    return render(request, 'clientes/lista_clientes.html', {})
