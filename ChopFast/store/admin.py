from django.contrib import admin
from .models import (Dish, Payments, Order, Delivery, OrderItem)

admin.site.register(Dish)
admin.site.register(Payments)
admin.site.register(Order)
admin.site.register(Delivery)
admin.site.register(OrderItem)

