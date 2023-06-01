from django.shortcuts import render, redirect, reverse
from .forms import Signin_Form, RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db import IntegrityError


""" This contains the definitions of the user sigin and register
    methods. 
    The signin() method and the register() method
"""


def signin(request):
    """ This method defines the signin method and user input sanitization """

    if request.method == 'POST':
        form = Signin_Form(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('wallet-details')
            else:
                messages.info(request, 'Invalid username or password.')
        else:
            messages.info(request, 'Invalid username or password!')
    else:
        form = Signin_Form()
        # messages.info(request, 'Please enter your username and password!.')


    return render(request, 'registration/login.html', {'form': form})



def register(request):
    """ This method defines the register method and user input sanitization """

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            try:
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password1']
                user = authenticate(request, username=username, email=email, password=password)
                login(request, user)
                return redirect('wallet-details')
            except IntegrityError and KeyError:
                messages.info(request, 'Invalid entries, try again')

        else:
            messages.info(request, 'Invalid entries, try again!')
    else:
        form = RegisterForm()
        # messages.info(request, 'Please enter your valid details!.')

    return render(request, 'registration/register.html', {'form': form})
