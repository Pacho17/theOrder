from django.db import models

# Create your models here.
class Pedido(models.Model):
    OBSERVACIONES_CHOICES=[
        ('sin salsas', 'sin Salsas'),
        ('con todas las salsas', 'Con Todas las Salsas'),
        ('sin salsa blanca', 'Sin Salsa Blanca'),
        ('con salsa blanca', 'Con Sslsa Blanca'),
        ('con mostaza', 'Con Mostaza'),
        ('sin mostaza', 'Sin Mostaza'),
        ('sin salsa roja', 'Sin Salsa Roja'),  
        ('con salsa roja', 'Con Salsa Roja'),
        ('sin cebolla', 'Sin Cebolla'),  
        ('sin pepinillos', 'Sin Pepinillos'),  
        
        
    ]

    PARALLEVAR_CHOICES = [
        ('si', 'Sí'),
        ('no', 'No')   
    ]

    ESTADO_CHOICES = [
        ('espera', 'En Espera'),  
        ('preparacion', 'En Preparación'),
        ('terminado', 'Terminado'),
    ]

  
    observaciones = models.CharField(max_length=50, choices=OBSERVACIONES_CHOICES,default='sin salsas')
    cantidad = models.PositiveIntegerField(default=0)  
    parallevar = models.CharField(max_length=50, choices=PARALLEVAR_CHOICES, default='si')  
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES, default='espera')  
    nombre_cliente = models.CharField(max_length=50, default='Cliente 1')

    def __str__(self):
        return self.nombre_cliente

