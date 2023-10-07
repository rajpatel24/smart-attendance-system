from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    readonly_fields = ('created', 'modified')
    search_fields = ('id', 'user__first_name', 'user__last_name', 'user__email', 'user__mobile',)
    ordering = ('id',)


admin.site.register(Employee, EmployeeAdmin)
