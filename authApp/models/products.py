from django.db import models


class Products(models.Model):
	idProducts = models.BigAutoField(primary_key=True)
	nombre = models.CharField("Nombre", max_length=255)		
	precio = models.IntegerField("Precio")
	inventario = models.IntegerField("Inventario")


