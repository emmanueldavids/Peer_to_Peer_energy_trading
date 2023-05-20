from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_Page),
    path('about/', views.about_page, name='about'),
]
