import signal
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User, AbstractUser
from django.db import models
import uuid
from datetime import timezone, datetime


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



class Transaction(models.Model):
    """ This is the transaction object that will be handling the buying and selling."""

    wallet = models.ForeignKey(Wallet, related_name="transactions", on_delete=models.PROTECT)
    transaction_id = models.AutoField(primary_key=True, editable='False')
    capacity = models.DecimalField(max_digits=10, decimal_places=1, default=0.0)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    start_time = models.TimeField()
    end_time = models.TimeField()
    


    @property
    def count_down(self):
        """ The count down method attribute returns the remaining time for the current transaction"""

        now = datetime.datetime.now().time()
        if self.end_time < now:
            return datetime.datetime.combine(datetime.date.today() + datetime.timedelta(days=1), self.end_time) - datetime.datetime.combine(datetime.date.today(), now)
        else:
            return datetime.datetime.combine(datetime.date.today(), self.end_time) - datetime.datetime.combine(datetime.date.today(), now)



    def __str__(self):
        """ Returns a string representation of this instance """

        return f"<{self.transaction_id}>"
    



class Payment(models.Model):
    """ This object will handle payments made from individual Wallet accounts."""

    wallet = models.ForeignKey(Wallet, related_name="payments", on_delete=models.PROTECT)
    payment_id = models.AutoField(primary_key=True, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    transaction = models.ForeignKey(Transaction, related_name="payments", on_delete=models.PROTECT)


    def __str__(self):
        """ Return a string representation of this instance"""

        return f"<{self.payment_id}, {self.timestamp}>"




class Logs(models.Model):
    """ This class object logs all Wallet transactions and Payments"""

    log_id = models.AutoField(primary_key=True)
    transaction = models.ForeignKey('Transaction', on_delete=models.PROTECT)
    payment = models.ForeignKey('Payment', on_delete=models.PROTECT)
    wallet = models.ForeignKey('Wallet', on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)



    def __str__(self):
        return f"Log ID: {self.log_id}"