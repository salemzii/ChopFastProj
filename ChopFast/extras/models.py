from django.db import models
from django.contrib.auth.models import User


class Tasks(models.Model):
    title = models.CharField(max_length=50)
    task = models.TextField()
    completed = models.BooleanField()


    def __str__(self):
        return self.title

# Create your models here.
