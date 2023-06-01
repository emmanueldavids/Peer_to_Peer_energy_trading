from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


""" Importing and applying the form definitions for 
    User Creation, login and Authentication
"""


class Signin_Form(forms.Form):
    """ This class represents the signin form for the user
        with all the authentication methods injected into it.
    """

    username = forms.CharField(label="Email", max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Enter UserName', 
        'class': 'form-control'
    }))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'form-control'
    }))




class RegisterForm(UserCreationForm):
    """ This class represents the user creation form 
        with all the authentication methods injected into it.
    """

    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
            'placeholder': 'User Name',
            'class': 'form-control'

        })) 
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={
            'placeholder': 'Valid Email', 
            'class': 'form-control'

        }))   
    password1 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={

            'placeholder': 'Enter Password',
            'class': 'form-control'
        }))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={

            'placeholder': 'Confirm Password',
            'class': 'form-control'
        }))

    
    class Meta:
        """ This is the Meta class for the User model."""

        model = User
        fields = ['username','email', 'password1', 'password2']
    

