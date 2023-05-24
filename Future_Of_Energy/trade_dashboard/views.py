from django.shortcuts import render
from django.http import HttpResponse

def dashboard(request):
    return render(request, 'dashboard/index.html')


def alert(request):
    return render(request, 'dashboard/alerts.html')


