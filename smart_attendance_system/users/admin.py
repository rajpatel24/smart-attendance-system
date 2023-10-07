from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.text import gettext_lazy as _

from .models import User


# Register your models here.


class DRFUserAdmin(UserAdmin):
    """
    Overrides UserAdmin
    """
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'mobile')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff',
                                       'is_superuser',
                                       )}),
        (_('Important dates'), {'fields': ('last_login', 'joined_date',
                                           'update_date')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name',
                       'email', 'mobile', 'groups',
                       'password1', 'password2'),
        }),
    )


admin.site.register(User, DRFUserAdmin)
