from django.shortcuts import render, reverse, HttpResponseRedirect
from kustom_user.models import Ticket
from kustom_user.forms import LoginForm, TicketForm, EditForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout


def homepage_view(request):
    html = "homepage.html"
    items = Ticket.objects.all().order_by('-status_of_ticket')
    return render(request, html, {'items': items})


@login_required()
def details_view(request, id):
    items = Ticket.objects.get(id=id)

    return render(request, "detailticket.html", {"items": items})


@login_required()
def create_ticket_view(request):
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
                status_of_ticket='New',
                user_assigned_to=None,
                user_who_completed=None
            )

            return HttpResponseRedirect(reverse("homepage"))

    form = TicketForm()

    return render(request, html, {'form': form})


@login_required()
def edit_ticket_view(request, id):
    html = "edit.html"

    if request.method == "POST":
        form = EditForm(request.POST)

        if form.is_valid():

            data = form.cleaned_data
            ticket = Ticket.objects.get(id=id)

            # When a ticket is assigned
            if data['user_assigned_to'] is not None:
                ticket.status_of_ticket = 'In-Progress'
                ticket.user_assigned_to = data['user_assigned_to']
                ticket.user_who_completed = None
                ticket.save()

            # When a ticket is Done
            elif data['status_of_ticket'] == "Done":
                ticket.status_of_ticket = "Done"
                ticket.user_assigned_to = None
                ticket.user_who_completed = data['user_who_completed']
                ticket.save()

            #  When a ticket is invalid
            elif data['status_of_ticket'] == "Invalid":
                ticket.status_of_ticket = "Invalid"
                ticket.user_assigned_to = None
                ticket.user_who_completed = None
                ticket.save()

        return HttpResponseRedirect(reverse("homepage"))

    form = EditForm()
    return render(request, html, {'form': form})


@login_required()
def user_tickets_view(request):

    user_items = Ticket.objects.filter(user_assigned_to=request.user)
    user_comp = Ticket.objects.filter(user_who_completed=request.user)
    tickets_filed = user_items.filter(user_who_filed=request.user)
    tickets_completed = user_comp.filter(status_of_ticket='Done')

    return render(request, "UserTickets.html",
                  {
                    'user_items': user_items,
                    'tickets_filed': tickets_filed,
                    'tickets_completed': tickets_completed
                   })


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


# def signup_view(request):
#     html = "signup.html"

#     if request.method == "POST":

#         form = SignupForm(request.POST)

#         if form.is_valid():

#             data = form.cleaned_data
#             MyKustomUser.objects.create_user(
#                 username=data['username'],
#                 email=data['email'],
#                 password=data['password']
#             )

#             return HttpResponseRedirect(reverse("homepage"))

#     form = SignupForm()

#     return render(request, html, {"form": form})
