# cuentas/models.py
from django.db import models

class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()
    id_tipcuenta = models.IntegerField(db_column='ID_TipCuenta', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuenta'
    