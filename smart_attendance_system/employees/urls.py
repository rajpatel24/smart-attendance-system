from django.urls import path
from rest_framework.routers import DefaultRouter


from .views import EmployeeViewset, EmployeeData, EmployeeDetectionTimestampViewset

router = DefaultRouter()

router.register(r'employee', EmployeeViewset, basename='employee')
router.register(r'employeeDetectionTimestamp', EmployeeDetectionTimestampViewset, basename='employee')

urlpatterns = router.urls

urlpatterns += [
    path('employee-data/', EmployeeData.as_view(), name='employee-data')
]
