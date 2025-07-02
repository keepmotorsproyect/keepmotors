from django.db import models

class Espacio(models.Model):
    ESTADO_CHOICES = [
        ('available', 'Disponible'),
        ('occupied', 'Ocupado'),
        ('reserved', 'Reservado'),
        ('maintenance', 'Mantenimiento'),
    ]

    VEHICULO_CHOICES = [
        ('', 'Sin tipo'),
        ('eléctrico', 'Eléctrico'),
        ('discapacitado', 'Discapacitado'),
        ('motocicleta', 'Motocicleta'),
    ]

    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='available')
    tipo_vehiculo = models.CharField(max_length=20, choices=VEHICULO_CHOICES, blank=True, default='')
    tarifa_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Espacio #{self.id} - {self.estado}"