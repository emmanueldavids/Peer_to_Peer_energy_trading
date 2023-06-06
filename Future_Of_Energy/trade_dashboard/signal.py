from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Wallet


@receiver(post_save, sender=User)
def create_user_wallet(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'wallet'):
        Wallet.objects.get_or_create(user=instance)
