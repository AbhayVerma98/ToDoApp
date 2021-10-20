from django.core import validators
from django import forms
from .models import User


class UserForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Name'}), required=True,
        max_length=50)
    email = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': "Email"}),
        required=True, max_length=50)
    password = forms.CharField(
        widget=forms.PasswordInput(render_value=True, attrs={'class': 'form-control form-control-sm', 'placeholder': "Password"}),
        required=True, max_length=50)

    class Meta:
        model = User
        fields = ['name', 'email', 'password']
