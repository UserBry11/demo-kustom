from django.urls import path
# from django.contrib import admin

from kustom_user import views

urlpatterns = [
    path('', views.homepage_view, name="homepage"),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('signup/', views.signup_view),
    path('ticket/', views.ticket_view),
    path('ticket/<int:id>/', views.edit_ticket_view)
]
