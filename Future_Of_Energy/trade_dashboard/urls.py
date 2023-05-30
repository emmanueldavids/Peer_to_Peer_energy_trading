from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('alert', views.alert, name='alert'),
    path('prices', views.prices, name='prices'),
    path('sell', views.sell_energy, name='sell'),
    path('feeds', views.feeds, name='feeds'),
    path('wallet', views.wallet, name='wallet'),
    path('transactions', views.transactions, name='transactions')
]
