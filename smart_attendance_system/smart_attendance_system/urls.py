from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('users.urls')),
]

admin.site.site_header = 'Smart Attendance System Administration'
admin.site.index_title = 'Smart Attendance System Admin'
admin.site.site_title = 'Smart Attendance System Administration'
