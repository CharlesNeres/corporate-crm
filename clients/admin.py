from django.contrib import admin
from .models import Client, Task

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "company", "status", "created_at")
    search_fields = ("name", "email", "company")
    list_filter = ("status", "created_at")

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "client", "priority", "status", "due_date", "created_at")
    search_fields = ("title", "client__name")
    list_filter = ("priority", "status", "due_date")