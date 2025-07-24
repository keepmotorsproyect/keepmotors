from django.db import models

# Create your models here.
class entrada (models.Model):
    tipo_vehiculo= models.TextField(("tipo_vehiuculo"))
    placa_vehiculo= models.TextField(("placa_vehiculo"))
    hora= models.TimeField(("hora"))
    dia= models.IntegerField(("dia"))
    mes = models.CharField("mes", max_length=20)
    login_id=models.IntegerField(("login"))
    
    