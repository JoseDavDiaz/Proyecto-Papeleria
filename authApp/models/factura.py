from django.db import models
from authApp.models.products import Products

class Factura(models.Model):
	idFactura = models.BigAutoField(primary_key=True)
	fecha = models.DateTimeField("Fecha", auto_now_add=True, blank=True)
	ctaVendidos = models.IntegerField("Cantidad de Productos", default=1)	
	valorCompra = models.IntegerField("Valor Total de Compra", default=1)
	idProducts = models.ForeignKey(Products, related_name='idProduct', on_delete=models.CASCADE)

	