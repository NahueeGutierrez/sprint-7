# cuentas/forms.py
from django import forms
from .models import Cuenta

class CrearCuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ['customer_id', 'balance', 'iban', 'id_tipcuenta']
