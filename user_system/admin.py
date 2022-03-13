from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, Permission

from user_system.models import User


class UserAdmin(UserAdmin):

    readonly_fields = ('password',)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'phone_number', 'password1', 'password2'),
        }),
    )

    class Meta:
        model = User


admin.site.register(User, UserAdmin)
admin.site.register(Permission)
