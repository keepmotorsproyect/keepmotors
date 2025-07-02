from django.db import models

class Espacio(models.Model):
    estado = models.CharField(max_length=20,default='available')
    tipo_vehiculo = models.CharField(max_length=20, blank=True, default='')
    placa_vehiculo= models.TextField(("placa_vehiculo"))
    tarifa_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Espacio #{self.id} - {self.estado}"