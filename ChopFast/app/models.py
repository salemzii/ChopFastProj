# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=120)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        template = f"Notifcation for {self.user}"
        return template.format(self)

