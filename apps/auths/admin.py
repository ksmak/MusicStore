from django.contrib import admin
from auths.models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser

    fieldsets = (
        ("Information", {
            "fields": [
                'email',
                'first_name',
                'last_name'
                'password',
            ]
        }),
        ("Permissions", {
            "fields": [
                'code',
                'is_superuser',
                'is_active',
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
                'first_name',
                'last_name',
                'password1',
                'password2',
                'is_active'
            ),
        }),
    )
    search_fields = (
        'email',
    )

    list_display = (
        'email',
        'is_active',
        'is_superuser'
    )

    readonly_fields = [
        'is_active',
        'code'
    ]

admin.site.register(CustomUser, CustomUserAdmin)
