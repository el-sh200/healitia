from django.contrib import admin

# Register your models here.
from .models import Subscriber


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    pass
