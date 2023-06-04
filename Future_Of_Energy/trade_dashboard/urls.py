from django.urls import path
from . import views


""" This is the application urls that defines the route to the
    resources path in views.
""" 


urlpatterns = [
    # path('', views.wallet_details, name='wallet-details'),
    path('', views.market_data, name='market-data'),
    path('trade', views.trade, name='trade'),
    # path('alert', views.alert, name='alert'),    
    # path('prices', views.prices, name='prices'),
    # path('market-data', views.market_data, name='market-data'),
    path('feeds', views.feeds, name='feeds'),
    path('wallet', views.wallet, name='wallet'),
    path('transactions', views.transactions, name='transactions'),
]
