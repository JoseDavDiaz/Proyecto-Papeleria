from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp import views
from authApp.views.ProductCreateView import ProductCreateView 
from authApp.views.ProductView import ProductsDetailView, ProductsListView, ProductUpdateView, ProductDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),  
    path('create/user/', views.UserCreateView.as_view()),
    path('user/<int:pk>', views.UserDetailView.as_view()),
    path('create/product/', ProductCreateView.as_view()),
    path('products/<int:pk>', ProductsDetailView.as_view()),
    path('products/list', ProductsListView.as_view()),
    path('products/update/<int:pk>', ProductUpdateView.as_view()),
    path('products/delete/<int:pk>', ProductDestroyView.as_view()),    
]
