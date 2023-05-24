from django.shortcuts import render
from django.http import HttpResponse

def wallet(request):
    return HttpResponse('{ Wallet: 1 }')