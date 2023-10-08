from django.urls import path
from rest_framework.routers import DefaultRouter


from .views import EmployeeViewset, EmployeeData, EmployeeDetectionTimestampViewset, EmployeeSummaryGeneration, \
    EmployeeOutDataEntry

router = DefaultRouter()

router.register(r'employee', EmployeeViewset, basename='employee')
router.register(r'employeeDetectionTimestamp', EmployeeDetectionTimestampViewset, basename='employee')

urlpatterns = router.urls

urlpatterns += [
    path('employee-data/', EmployeeData.as_view(), name='employee-data'),
    path('employee-out-data/', EmployeeOutDataEntry.as_view(), name='employee-out-data'),
    path('employee-summary/', EmployeeSummaryGeneration.as_view(), name='employee-summary')
]
