from django.contrib import admin
from .models import User, Wallet, Payment, Transaction, Logs


"""Register all models by creating admin classes that inherit from admin.ModelAdmin """


# @admin.register(User, Wallet, Transaction, Payment, Logs)
# class MyModelAdmin(admin.ModelAdmin):
#     pass



@admin.register(User)
class UserDashboard(admin.ModelAdmin):
    """ This class registers the User model to the Admin interface"""

    list_display = [
        'id', 
        'username', 
        'email', 
        'is_staff', 
        'is_superuser'
        ]


@admin.register(Wallet)
class UserWallet(admin.ModelAdmin):
    """ This class registers the Wallet Model to the Admin interface"""

    list_display = [
        'user_id', 
        'wallet_id',
        'balance', 
        'previous_balance',
        'currency', 
        'created_at', 
        'updated_at', 
        'status'
        ]
    

@admin.register(Payment)
class UserPayment(admin.ModelAdmin):
    """ This class registers the payment Model to the admin interface """

    list_display = [
        'payment_id',
        'wallet_id',
        'transaction_id',
        'timestamp'
    ]



@admin.register(Transaction)
class PaymentTransaction(admin.ModelAdmin):
    """ This class registers the Transaction object to the admin interface """

    list_display = [
        'transaction_id',
        'wallet_id',
        'capacity',
        'amount',
        'start_time',
        'end_time',
    ]


@admin.register(Logs)
class All_Logs(admin.ModelAdmin):
    """ This class registers the Logs object to the admin interface """

    list_display = [
        'log_id',
        'transaction_id',
        'payment_id',
        'wallet_id',
        'user_id',
        'timestamp'
    ]