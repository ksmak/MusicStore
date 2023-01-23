from django.contrib import admin
from auths.models import MyUser

class MyUserAdmin(admin.ModelAdmin):
    model = MyUser

    add_fieldsets = (
        ('Personal date', {
            'classes':(
                'wide'
            ),
            'fields': (
                'email',
                'first_name',
                'last_name',
                'middle_name',
                'password1',
                'password2'
            )

        }),
        ('Permissions', {
            'classes': (
                'wide'
            ),
            'fields': (
                'is_active',
                'is_superuser',
                'groups'
            )
        })
    )

    fieldsets = (
        ('Personal data', {
            'fields': (
                'email',
                'first_name',
                'last_name',
                'middle_name',
                'password',
            )
        }),
        ('Permisions', {
            'fields': (
                'is_active',
                'is_superuser',
                'groups'
            )
        })
    )

    list_display = (
        'email',
        'first_name',
        'last_name',
        'middle_name',
        'is_active',
        'is_staff',
        'is_superuser'
    )

    search_fields = (
        'email',
        'first_name',
        'last_name',
        'middle_name'
    )

    ordering = (
        'email',
        'first_name',
        'last_name',
        'middle_name'
    )


admin.site.register(MyUser, MyUserAdmin)
