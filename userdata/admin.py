from django.contrib import admin
from .models import CustomUser
from .forms import CustomForm
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomForm
    list_display = ('username', 'email', 'first_name',
                    'last_name', 'is_staff', 'is_teacher', 'is_student')

    fieldsets = (
        *UserAdmin.fieldsets, (
            'User Types',
            {
                'fields': (
                    'is_teacher',
                    'is_student'
                )
            }
        )
    )


admin.site.register(CustomUser, CustomUserAdmin)
