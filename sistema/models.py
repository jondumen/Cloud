from django.db import models

class Habitacion(models.Model):
    TIPO_CHOICES = [
        ('individual', 'Individual'),
        ('doble', 'Doble'),
        ('doble_balcon', 'Doble con Balcón'),
        ('triple', 'Triple'),
        ('cuadruple', 'Cuádruple'),
        ('terraza', 'Con Terraza'),
        ('piscina', 'Con Piscina'),
        ('familiar', 'Familiar'),
        ('suite', 'Suite'),
    ]

    ESTADO_CHOICES = [
        ('disponible', 'Disponible'),
        ('no_disponible', 'No disponible'),
        ('fuera_de_servicio', 'Fuera de servicio'),
    ]

    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    pais = models.CharField(max_length=100)
    
class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    habitacion_id = models.IntegerField()
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    estado_pago = models.CharField(max_length=100)

class Informe(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
