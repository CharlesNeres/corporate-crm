from django.contrib import admin
from .models import Client

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "company", "status", "created_at")
    search_fields = ("name", "email", "company")
    list_filter = ("status", "created_at")
