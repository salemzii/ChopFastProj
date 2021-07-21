from django.db import models
from django.contrib.auth.models import User

from profiles.models import Customer
from django.utils import timezone

from PIL import Image
import uuid


class Dish(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField(default='defaultdish.png')
    price = models.IntegerField(default=1500)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except Exception as err:
            url = ''
        return url


class Payments(models.Model):
    id = models.CharField(max_length=18,
                primary_key=True,
                editable=False)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=60)
    amount = models.IntegerField(default=1500)
    verified = models.BooleanField(default=False)
    time = models.DateTimeField(default=timezone.now)


    def __str__(self):
        template = f"{self.name.username}'s payment."
        return template.format(self)



class Order(models.Model):
    id = models.UUIDField(default=uuid.uuid4,
                        primary_key=True,
                        editable=False)
                        
    customer = models.ForeignKey(Customer, 
    on_delete=models.SET_NULL, null=True)
    time = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)


    def __str__(self):
        template = f"Order id {self.id}"
        return template.format(self)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property 
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total =self.dish.price * self.quantity
        return total


class Delivery(models.Model):

    STATUS_CHOICES = (
        ('In-Progress', 'In-Progress'),
        ('Completed', 'Completed')
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete= models.CASCADE)
    rider = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    delivered = models.BooleanField(default=False)
    confirm_delivery = models.BooleanField(default=False)
    time = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20,
     choices=STATUS_CHOICES)


    def __str__(self):
         return self.status


class Restaurant(models.Model):
    name = models.CharField(max_length=120, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=220, blank=False)
    rating = models.IntegerField(default=0)
    menus = models.ForeignKey(Dish, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Wallet(models.Model):
    id = models.CharField(max_length=18,
                primary_key=True,
                editable=False)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    balance = models.FloatField(default=0.00)

#www.simpleisbetterthancomplex.com