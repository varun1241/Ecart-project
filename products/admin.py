from django.contrib import admin

# Register your models here.
from .models import Product,Student


admin.site.register(Product)

admin.site.register(Student)