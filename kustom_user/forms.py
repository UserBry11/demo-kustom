from django import forms
# from django.contrib.auth.forms import UserCreationForm
from kustom_user.models import MyKustomUser, Ticket


# class Login_Form(forms.ModelForm):

#     class Meta:
#         model = MyKustomUser
#         fields = ['username', 'email']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'date_filed', 'description', 'user_who_filed', 'status_of_ticket', 'user_assigned_to', 'user_who_completed']


class EditForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'date_filed', 'description', 'user_who_filed', 'status_of_ticket', 'user_assigned_to', 'user_who_completed']
