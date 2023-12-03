# from django.db import models

# <<<<<<< HEAD

# class Prestamo(models.Model):
#     loan_id = models.AutoField(primary_key=True)
#     loan_type = models.TextField()
#     loan_date = models.TextField()
#     loan_total = models.IntegerField()
#     customer_id = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'prestamo'


# class Tiposclientes(models.Model):
#     id_tipcliente = models.TextField(db_column='ID_TipCliente', primary_key=True)  # Field name made lowercase. This field type is a guess.
#     nombre = models.CharField(db_column='NOMBRE',max_length=255)  # Field name made lowercase.

#     def __str__(self):
#         return self.nombre
    
#     class Meta:
#         managed = False
#         db_table = 'TiposClientes'


