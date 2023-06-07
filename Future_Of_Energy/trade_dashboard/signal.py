from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Wallet, Transaction, Payment, Logs


@receiver(post_save, sender=User)
def create_user_wallet(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'wallet'):
        Wallet.objects.get_or_create(user=instance)


triggers = ['User', 'Wallet', 'Transaction', 'Payment']

for trigger in triggers:

    @receiver(post_save, sender=trigger)
    def create_user_logs(sender, instance, created, **kwargs):
        if created and not hasattr(instance, 'logs'):
            Logs.objects.get_or_create(trigger=instance)

