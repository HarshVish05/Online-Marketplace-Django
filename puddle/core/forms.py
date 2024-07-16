from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    """ By inheriting from UserCreationForm, SignUpForm automatically includes fields and 
    functionality for handling user creation, such as username, password1, 
    and password2 (for password confirmation)."""
    class Meta:
        #  The Meta class is used to configure specific options for the form.
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    username = forms.CharField(widget= forms.TextInput(attrs= {
        'placeholder': 'Enter your name',
        'class': 'py-4 px-6 w-full rounded-xl'
    }))
    
    email = forms.CharField(widget= forms.EmailInput(attrs= {
        'placeholder': 'Enter your Email',
        'class': 'py-4 px-6 w-full rounded-xl'
    }))
    
    password1 = forms.CharField(widget= forms.PasswordInput(attrs= {
        'placeholder': 'Enter your password',
        'class': 'py-4 px-6 w-full rounded-xl'
    }))
    password2 = forms.CharField(widget= forms.PasswordInput(attrs= {
        'placeholder': 'Re-type your password',
        'class': 'py-4 px-6 w-full rounded-xl'
    }))


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget= forms.TextInput(attrs={
        'placeholder': "Enter your username",
        "class": "py-4 px-6 w-full rounded-xl"
    }))
    
    password = forms.CharField(widget= forms.PasswordInput(attrs={
        'placeholder': "Enter your password",
        "class": "py-4 px-6 w-full rounded-xl"
    }))