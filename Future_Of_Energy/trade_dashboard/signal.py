from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Wallet, Transaction, Payment, Logs


@receiver(post_save, sender=User)
def create_user_wallet(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'wallet'):
        Wallet.objects.get_or_create(user=instance)



@receiver(post_save, sender=User)
@receiver(post_save, sender=Wallet)
@receiver(post_save, sender=Transaction)
@receiver(post_save, sender=Payment)

def create_user_logs(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'logs'):
        Logs.objects.create(
            transaction=instance if isinstance(instance, Transaction) else None,
            payment=instance if isinstance(instance, Payment) else None,
            wallet=instance if isinstance(instance, Wallet) else None,
            user=instance if isinstance(instance, User) else None,
        )