from django.contrib import admin
from .models import Cart , User, Order, Product, Sort, SubSort

# Register your models here.
admin.site.register(Cart)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Sort)
admin.site.register(SubSort)
