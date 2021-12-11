from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainSerializer

from authApp.serializers.productSerializer import ProductSerializer

class ProductCreateView(views.APIView):
	def post(self, request, *args, **kwargs):
		serializer = ProductSerializer(data = request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()

		tokenData = {				
				"Nombre" : request.data["nombre"],
				"Precio" : request.data["precio"],
				"Inventario"  : request.data["inventario"]
		}
		try:
			toknSerializer = TokenObtainSerializer(data = tokenData)
			toknSerializer.is_valid(raise_exception=True)
			return Response(tokenData.validated_data, status=status.HTTP_201_CREATED)			
		except Exception as e:
			return Response('Producto Creado Exitosamente', status=status.HTTP_201_CREATED)