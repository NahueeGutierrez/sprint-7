from django import forms

class BusquedaClienteForm(forms.Form):
    cliente_id = forms.IntegerField(label='Ingrese el ID del Cliente')
