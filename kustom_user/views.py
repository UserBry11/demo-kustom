from django.shortcuts import render, reverse, HttpResponseRedirect
from kustom_user.models import MyKustomUser, Ticket
from kustom_user.forms import LoginForm, SignupForm, TicketForm, EditForm

from django.contrib.auth import login, authenticate, logout


def homepage_view(request):
    html = "homepage.html"
    items = Ticket.objects.all()
    return render(request, html, {'items': items})


def ticket_view(request):
    html = "ticket.html"

    if request.method == "POST":
        form = TicketForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            Ticket.objects.create(
                title=data['title'],
                date_filed=data['date_filed'],
                description=data['description'],
                user_who_filed=request.user,
                status_of_ticket=data['status_of_ticket'],
                user_assigned_to=data['user_assigned_to'],
                user_who_completed=data['user_who_completed']
            )

            return HttpResponseRedirect(reverse("homepage"))

    form = TicketForm()

    return render(request, html, {'form': form})


def edit_ticket_view(request, id):
    html = "edit.html"
    form = EditForm()
    return render(request, html, {'form': form})


def login_view(request):
    html = "login.html"

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
                )
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', '/'))
    else:
        form = LoginForm()
    return render(request, html, {
        'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))


def signup_view(request):
    html = "signup.html"

    if request.method == "POST":

        form = SignupForm(request.POST)

        if form.is_valid():

            data = form.cleaned_data
            MyKustomUser.objects.create_user(
                username=data['username'],
                email=data['email'],
                password=data['password']
            )

            return HttpResponseRedirect(reverse("homepage"))

    form = SignupForm()

    return render(request, html, {"form": form})
