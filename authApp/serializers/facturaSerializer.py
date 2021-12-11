from rest_framework import request, serializers
from authApp.models.factura import Factura
from authApp.models.products import Products

class FacturaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Factura
		fields = ['idFactura', 'fecha', 'ctaVendidos','valorTotal','idProducts','nombre','precio']


	def to_representation(self, obj):
		factura = Factura.objects.get(id = obj.id)
		products = Products.objects.get(id = obj.products_id)
		return{
			"idFactura": factura.idFactura,
			"fecha": factura.fecha,
			"ctaVendidos": factura.ctaVendidos,
			"valorTotal": factura.valorCompra,
			"Products": {				
				"nombre" : products.nombre,
				"precio": products.precio,			
			}
		}