from django.contrib import admin
from auths.models import MyUser

class MyUserAdmin(admin.ModelAdmin):
    model = MyUser

    list_display = (
        'username',
        'email',
        'is_active',
        'is_staff',
        'is_superuser'
    )

admin.site.register(MyUser, MyUserAdmin)
