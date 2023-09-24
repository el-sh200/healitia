# Django Built-in modules
from django.contrib import admin

# Local apps
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
