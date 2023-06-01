"""Future_Of_Energy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


""" This is the project defined urls that specify the 
    path to load the resources.
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('energy_trading.urls')),
    path('wallet/', include('payment_wallet.urls')),
    path('dashboard/', include('trade_dashboard.urls')),
    path('accounts/', include('accounts.urls')),
]
