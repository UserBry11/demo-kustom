from django import forms
from django.contrib.auth.forms import UserCreationForm
from kustom_user.models import MyKustomUser


# class Login_Form(forms.ModelForm):

#     class Meta:
#         model = MyKustomUser
#         fields = ['username', 'email']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)


class SignupForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.CharField(max_length=30)