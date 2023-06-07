import signal
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User, AbstractUser
from django.db import models
import uuid


""" Creating the class objects for the database and defining the tables objects and relationship.
    For this model file, we will create the object for wallet, payment, market_data,
    transactions and logs.
"""


class User(AbstractUser):
    """Customizing the User field to auto create the Wallet object anytime a new user is created """
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        if not hasattr(self, 'wallet'):
            Wallet.objects.create(user=self)




class Wallet(models.Model):
    """ This class inheriting from the model object is responsible to create wallet table."""
    
    CURRENCY_CHOICES = (
        ('USD', _('US Dollars')),
        ('GHS', _('Ghana Cedis')),
        ('EUR', _('Euro')),
        ('GBP', _('British Pounds')),
        ('BTC', _('Bit Coins'))
    )

    STATUS_CHOICES = (
        ('active', _('Active')),
        ('inactive', _('Inactive')),
        ('pending', _('Pending')),
    )

    is_authenticated = True
    REQUIRED_FIELDS = ('balance', 'currency')
    USERNAME_FIELD = 'user'
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wallet_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    previous_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default="BTC")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    

    @property
    def is_anonymous(self):
        """
        Always return False. This is a way of comparing User objects to
        anonymous users.
        """
        return False


    def __repr__(self):
        """ This method returns a string representation of this instance"""
        return f"<{self.wallet_id}>"


    def save(self, *args, **kwargs):
        """ This method calls and overwrites the save method with additional parameters """
        created = self.pk
        if not self.balance and not self.currency:
            raise ValueError('balance and currency fields are required!')

        if self.balance > 0 and self.status != 'active': # sets status to active once a new account is created
            self.status = 'active'
        
        else:
            try:
                previous_wallet = Wallet.objects.get(pk=self.pk)
                if self.balance != previous_wallet.balance:
                    self.previous_balance = previous_wallet.balance
        
            except Wallet.DoesNotExist:
                pass
        
        super().save(*args, **kwargs)