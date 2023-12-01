from django.db import models


class Tiposclientes(models.Model):
    id_tipcliente = models.TextField(db_column='ID_TipCliente', primary_key=True)  # Field name made lowercase. This field type is a guess.
    nombre = models.CharField(db_column='NOMBRE',max_length=255)  # Field name made lowercase.

    def __str__(self):
        return self.nombre
    
    class Meta:
        managed = False
        db_table = 'TiposClientes'

# class Cliente(models.Model):
#     customer_id = models.AutoField(primary_key=True)
#     customer_name = models.TextField()
#     customer_surname = models.TextField()  # This field type is a guess.
#     customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
#     dob = models.TextField(blank=True, null=True)
#     branch_id = models.IntegerField()
#     ID_TipCliente = models.ForeignKey(Tiposclientes, on_delete=models.CASCADE)
    
#     def __str(self):
#         return self.customer_dni
    
#     class Meta:
#         managed = False
#         db_table = 'cliente'
 
# INTENTE REALIZAR LA BUSQUEDA MEDIANTE UN FOREING KEY DE CLIENTES PERO NOSE ACTUALIZABA EN LA BASE DE DATOS POR LO TANTO NO ME REALIZABA LA BUSQUEDA Y LO TUVE QUE REALIZAR POR ID_TIPOCLIENTE QUE ESTABA DENTRO DE LA MISMA TABLA