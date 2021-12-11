from django.conf                                  import settings
from django.db.models.query import QuerySet
from rest_framework import generics, status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import Serializer
from rest_framework_simplejwt.backends	import TokenBackend

from authApp.models.products import Products
from authApp.serializers.productSerializer import ProductSerializer


class ProductsDetailView(generics.RetrieveAPIView):
	queryset = Products.objects.all()
	serializer_class = ProductSerializer
	
	def retrieve(self, request, *args, **kwargs):
		return super().retrieve(request, *args, **kwargs)

class ProductsListView(generics.ListAPIView):
	queryset = Products.objects.all()
	serializer_class = ProductSerializer

	def list(self, request, *args, **kwargs):
		return super().list(request, *args, **kwargs)

class ProductUpdateView(generics.UpdateAPIView):
	queryset = Products.objects.all()
	serializer_class = ProductSerializer

	def update(self, request, *args, **kwargs):
		return super().update(request, *args, **kwargs)


class ProductDestroyView(generics.RetrieveDestroyAPIView):
	queryset = Products.objects.all()	
	serializer_class = ProductSerializer	

	def destroy(self, request, *args, **kwargs):
	
		return super().destroy(request, *args, **kwargs)
