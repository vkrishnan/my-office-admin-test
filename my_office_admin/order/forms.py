from .models import Customer
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('contact_number', 'address')