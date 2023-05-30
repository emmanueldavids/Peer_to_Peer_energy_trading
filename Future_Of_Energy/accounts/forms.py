from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class Signin_Form(forms.Form):
    username = forms.CharField(label="Email", max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Enter UserName', 
        'class': 'form-control'
    }))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'form-control'
    }))




class RegisterForm(UserCreationForm):
    error_messages = {
        'username_taken': 'This username is already taken.',
        'password_too_short': 'Password should be at least 8 characters long.',
    }
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
        model = User
        fields = ['username','email', 'password1', 'password2']
    

