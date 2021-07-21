from django.db.models.signals import post_save
from .models import Payments, Order
from django.dispatch import receiver 


@receiver(post_save, sender=Payments)
def create_order(sender, instance, created, **kwargs):
    if created:
        Order.objects.create(payment=instance)


@receiver(post_save, sender=Payments)
def save_order(sender, instance, **kwargs):
    instance.order.save()