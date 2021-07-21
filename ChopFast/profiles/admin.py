from django.contrib import admin
from .models import Customer, Rider, Supplier, Staff

admin.site.register(Customer)
admin.site.register(Rider)
admin.site.register(Staff)
admin.site.register(Supplier)


# Register your models here.
