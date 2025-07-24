from django.db import models

# Create your models here.
class registro (models.Model):
    nombre_completo= models.TextField(("nombre_completo"))
    correo_electronico= models.TextField(("correo_electronico"))
    telefono= models.IntegerField(("telefono"))
    placa_de_vehiculo= models.TextField(("placa_de_vehiculo"))
    contraseña= models.TextField(("contraseña"))
    confirmar_contraseña= models.TextField(("confirmar_contraseña"))
    