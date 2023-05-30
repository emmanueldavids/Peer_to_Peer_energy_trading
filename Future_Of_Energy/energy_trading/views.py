from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def landing_Page(request):
    return render(request, 'energy_trading/index.html')

def about_page(request):
    return render(request, 'energy_trading/about.html')

def contact_page(request):
    return render(request, 'energy_trading/contact.html')

