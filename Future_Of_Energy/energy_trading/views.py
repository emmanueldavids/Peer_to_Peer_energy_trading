from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "energy_trading/index.html")

def ticket(request):
    return render(request, "energy_trading/ticket.html")