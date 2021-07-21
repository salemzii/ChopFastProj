from django.db import models
from PIL import Image
from django.contrib.auth.models import User
import uuid


class Customer(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image= models.ImageField(default = 'default.jpg', blank=True, upload_to='profile_pics')
    address = models.CharField(max_length=75)
    phone_number = models.CharField(max_length=11)


    def __str__(self):
        template = f"{self.user.username}'s profile."
        return template.format(self)


class Rider(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key= True,
        editable=False
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default= 'default.jpg', upload_to='profile_pics')
    address = models.CharField(max_length=75)
    is_active = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=11)


    def __str__(self):
        template = f"{self.user.username}'s profile."
        return template.format(self)


class Staff(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True, 
        editable=False
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    address = models.CharField(max_length=75)
    is_active = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        template = f"{self.user.username}'s profile."
        return template.format(self)


class Supplier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=220)
    phone_number = models.CharField(max_length=11)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        template = f"{self.user.username}'s profile."
        return template.format(self)

# Create your models here.
