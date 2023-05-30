from django.shortcuts import render


def dashboard(request):
    return render(request, 'dashboard/index.html')


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