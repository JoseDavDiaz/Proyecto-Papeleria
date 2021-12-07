from django.contrib import admin
from .models.user import User
from .models.products import Products
from .models.factura import Factura
# Register your models here.

admin.site.register(User)
admin.site.register(Products)
admin.site.register(Factura)