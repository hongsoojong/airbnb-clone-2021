from django import forms
from django.core import exceptions
from . import models

class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data("email")
        try:
            models.User.objects.get(username=email)
            return email
        except models.User.DoesNotExist:
            raise forms.ValidationError("User does not exist")

    def clean_password(self):
        email = self.cleaned_data("email")
        password = self.cleaned_data("password")
        try:
            user = models.User.objects.get(username=email)
            if user.check_password(password):
                return password
            else forms.exceptions.ValidationError("Password is wrong")
        except models.User.DoesNotExist:
            pass
        
