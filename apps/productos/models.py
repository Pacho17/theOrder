from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre_producto = models.CharField(max_length=100)
    precio_producto= models.DecimalField(max_digits=10, decimal_places=3,default=0)
    descripcion=models.TextField()
    
    def __str__(self):
        return self.nombre_producto