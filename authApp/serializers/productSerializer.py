from rest_framework import serializers
from authApp.models.products import Products

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Products
		fields = ['id', 'nombre', 'precio', 'inventario']

	def to_representation(self, obj):
		products = Products.objects.get(id = obj.id)
		return {
			'id' : products.id,
			'nombre' : products.nombre,
			'precio' : products.precio,
			'inventario' : products.inventario 
		}
	
	def create(self, validated_data):
		productInstance = Products.objects.create(**validated_data)
		return productInstance
