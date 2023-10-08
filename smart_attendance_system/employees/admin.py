from django.contrib import admin
from .models import Employee, EmployeeDetectionTimeStamp, EmployeeDetectionOutTimeStamp


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    readonly_fields = ('created', 'modified')
    search_fields = ('id', 'user__first_name', 'user__last_name', 'user__email', 'user__mobile',)
    ordering = ('id',)


class EmployeeDetectionTimestampAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee')
    readonly_fields = ('created', 'modified')
    search_fields = ('id', 'employee__user__first_name', 'employee__user__last_name',
                     'employee__user__email', 'employee__user__mobile',)
    ordering = ('id',)


class EmployeeDetectionOutTimestampAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee')
    readonly_fields = ('created', 'modified')
    search_fields = ('id', 'employee__user__first_name', 'employee__user__last_name',
                     'employee__user__email', 'employee__user__mobile',)
    ordering = ('id',)


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(EmployeeDetectionTimeStamp, EmployeeDetectionTimestampAdmin)
admin.site.register(EmployeeDetectionOutTimeStamp, EmployeeDetectionOutTimestampAdmin)
