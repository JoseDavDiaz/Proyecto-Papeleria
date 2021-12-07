from django.db import models
from authApp.models.products import Products

class Factura(models.Model):
	idFactura = models.BigAutoField(primary_key=True)
	fecha = models.DateTimeField("Fecha" )
	ctaVendidos = models.IntegerField("Productos vendidos", default=1)
	idProducts = models.ForeignKey(Products, related_name='idProduct', on_delete=models.CASCADE)
