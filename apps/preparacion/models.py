from django.db import models
from apps.pedidos.models import Pedido
from apps.productos.models import Producto
from apps.detalles.models import DetallePedido
# Create your models here.

class AreaPreparacion(models.Model):
    pedido =models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True)
    producto=models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad= models.ForeignKey(DetallePedido, on_delete=models.SET_NULL, null=True)
    estado= models.CharField(max_length=20, choices=[
        ('espera','En Espera'),
        ('preparacion','En Preparacion'),
        ('terminado','Terminado'),
        
    ], default='preparacion')
    
    def __str__(self):
        return f"pedido:{self.pedido.nombre_cliente},producto:{self.producto.nombre_producto}, cantidad:{self.cantidad.cantidad}, Para Llevar:{self.pedido.parallevar}, estado:{self.estado}"
    