from django.shortcuts import render
from django.contrib import messages



def wallet_details(request):
    return render(request, 'wallet-info/wallet-details.html', {'message': messages})
    

def trade(request):
    return render(request, 'dashboard/trade.html')


def alert(request):
    return render(request, 'dashboard/alerts.html')


def prices(request):
    return render(request, 'dashboard/prices.html')


def sell_energy(request):
    return render(request, 'dashboard/sell-energy.html')


def feeds(request):
    return render(request, 'dashboard/feeds.html')


def wallet(request):
    return render(request, 'dashboard/wallet.html')


def transactions(request):
    return render(request, 'dashboard/transactions.html')