from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def landing_Page(request):
    return render(request, 'energy_trading/landing_page.html')