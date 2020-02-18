from django.shortcuts import render, reverse, HttpResponseRedirect
from kustom_user.models import MyKustomUser
from kustom_user.forms import LoginForm, SignupForm

from django.contrib.auth import login, authenticate, logout


def homepage_view(request):
    html = "homepage.html"

    return render(request, html)


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
#             user = User.objects.create_user(
#                 data['username'],
#                 data['email']
#             )

#             login(request, user)
#             MyKustomUser.objects.create(
#                 name=data['username'],
#                 user=user
#             )

#             return HttpResponseRedirect(reverse("homepage"))

#     form = SignupForm()

#     return render(request, html, {"form": form})
