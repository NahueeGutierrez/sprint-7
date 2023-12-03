from django import forms

class BusquedaClienteForm(forms.Form):
    cliente_id = forms.IntegerField(label='Ingrese el ID del Cliente (recuerda que hay clientes que no tiene cuentas)')
