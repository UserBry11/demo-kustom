from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from kustom_user.models import MyKustomUser

# Register your models here.
admin.site.register(MyKustomUser, UserAdmin)
