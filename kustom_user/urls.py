from django.urls import path
# from django.contrib import admin

from kustom_user import views

urlpatterns = [
    path('', views.homepage_view, name="homepage"),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('create_ticket/', views.create_ticket_view),
    path('ticket/<int:id>/', views.details_view),
    path('ticket/<int:id>/edit/', views.edit_ticket_view),
    path('user_tickets/', views.user_tickets_view)
]
