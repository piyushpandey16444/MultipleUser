from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ["username", "first_name",
                    "last_name", "is_teacher", "is_student"]
    list_display_links = ["username", "first_name", "last_name", "is_teacher", "is_student"]
