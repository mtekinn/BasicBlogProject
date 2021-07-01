from django import forms
from django.forms.widgets import PasswordInput

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label="Username")
    password = forms.CharField(max_length=20, label="Password", widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=20, label="Confirm Password", widget=forms.PasswordInput)

    
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords does not match each other!")

        values = {
            "username": username,
            "password": password,
            # "confirm_password": confirm_password
        }
        return values


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label="Username")
    password = forms.CharField(max_length=20, label="Password", widget=forms.PasswordInput)


