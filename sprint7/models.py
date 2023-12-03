# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Marcastarjeta(models.Model):
    id_martarjeta = models.TextField(db_column='ID_MarTarjeta', primary_key=True)  # Field name made lowercase. This field type is a guess.
    nombre = models.CharField(db_column='Nombre')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MarcasTarjeta'


class Tarjeta(models.Model):
    id_tarjeta = models.TextField(db_column='ID_Tarjeta', primary_key=True, blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    numero = models.CharField(db_column='Numero')  # Field name made lowercase.
    cvv = models.CharField(db_column='CVV')  # Field name made lowercase.
    fechaotorgamiento = models.CharField(db_column='FechaOtorgamiento')  # Field name made lowercase.
    fechaexpiracion = models.CharField(db_column='FechaExpiracion')  # Field name made lowercase.
    id_customer = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='ID_Customer', blank=True, null=True)  # Field name made lowercase.
    id_martarjeta = models.ForeignKey(Marcastarjeta, models.DO_NOTHING, db_column='ID_MarTarjeta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tarjeta'


class Tiposclientes(models.Model):
    id_tipcliente = models.TextField(db_column='ID_TipCliente', primary_key=True)  # Field name made lowercase. This field type is a guess.
    nombre = models.CharField(db_column='NOMBRE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TiposClientes'


class AuditoriaCuenta(models.Model):
    old_id = models.IntegerField(blank=True, null=True)
    new_id = models.IntegerField(blank=True, null=True)
    old_balance = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    new_balance = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    old_iban = models.CharField(blank=True, null=True)
    new_iban = models.CharField(blank=True, null=True)
    old_type = models.CharField(blank=True, null=True)
    new_type = models.CharField(blank=True, null=True)
    user_action = models.CharField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'auditoria_cuenta'


class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cliente'


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()
    id_tipcuenta = models.IntegerField(db_column='ID_TipCuenta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cuenta'


class Direcciones(models.Model):
    id_direc = models.TextField(db_column='ID_Direc', primary_key=True, blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    direccion = models.CharField(db_column='Direccion', blank=True, null=True)  # Field name made lowercase.
    employee = models.ForeignKey('Empleado', models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey(Cliente, models.DO_NOTHING, blank=True, null=True)
    branch = models.OneToOneField('Sucursal', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direcciones'


class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI')  # Field name made lowercase.
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'empleado'


class Movimientos(models.Model):
    numero_cuenta = models.IntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    tipo_operacion = models.CharField(blank=True, null=True)
    hora = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'movimientos'


class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prestamo'


class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sucursal'


class Tiposcuenta(models.Model):
    id_tipcuenta = models.TextField(db_column='ID_TipCuenta', primary_key=True)  # Field name made lowercase. This field type is a guess.
    nombre = models.CharField(db_column='Nombre')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tiposCuenta'
