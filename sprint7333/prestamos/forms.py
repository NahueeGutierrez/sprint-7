from django import forms
from .models import *


class CrearPrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['loan_id','loan_type', 'loan_date', 'loan_total', 'customer_id']