from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from auths.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = (
        ("Information", {
            "fields": [
                'email',
                'first_name',
                'last_name',
                'password',
            ]
        }),
        ("Permissions", {
            "fields": [
                'code',
                'is_active',
                'is_staff',
                'is_superuser',
            ]
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': (
                'wide',
            ),
            'fields': (
                'email',
                'password1',
                'password2',
                'is_active',
            ),
        }),
    )
    
    search_fields = (
        'email',
    )

    readonly_fields = (
        'code',
        'is_active',
        'is_staff',
        'is_superuser',
    )
    
    list_filter = (
        'email',
        'first_name',
        'last_name'
    )

    list_display = (
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_superuser'
    )

    ordering = (
        'email',
    )

admin.site.register(CustomUser, CustomUserAdmin)
