from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainSerializer

from authApp.serializers.facturaSerializer import FacturaSerializer

class FacturaCreateView(views.APIView):
	def post(self, request, *args, **kwargs):
		serializer = FacturaSerializer(data = request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
