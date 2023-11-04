from django.contrib import admin
from user.models import UserModel

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "fullname", "username", "email", "mobile", "password")


admin.site.register(UserModel, UserAdmin)
