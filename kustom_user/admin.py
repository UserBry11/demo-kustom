from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from kustom_user.models import MyKustomUser, Ticket

# Register your models here.
admin.site.register(MyKustomUser, UserAdmin)
admin.site.register(Ticket)
