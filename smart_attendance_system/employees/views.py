import time
from datetime import datetime

from django.http import Http404
from rest_framework.response import Response
from rest_framework import viewsets, authentication,permissions, status
from rest_framework.views import APIView
from django.utils import timezone

from .serializers import EmployeeSerializer, EmployeeDetectionTimestampSerializer
from .models import Employee, EmployeeDetectionTimeStamp, EmployeeDetectionOutTimeStamp


from django.db.models import Sum, F, ExpressionWrapper, fields
from django.utils.timezone import make_aware
from django.db.models.functions import ExtractMonth
from datetime import datetime


class EmployeeViewset(viewsets.ModelViewSet):
    http_method_names = [u'get', u'post', u'put']
    serializer_class = EmployeeSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Employee.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(
            {
                'message': 'Employees List',
                'success': True,
                'status': status.HTTP_200_OK,
                'data': serializer.data
            }
        )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        return Response(
            {
                'message': 'Employee Details',
                'success': True,
                'status': status.HTTP_200_OK,
                'data': serializer.data
            }
        )

    def create(self, request, *args, **kwargs):
        """
        This method creates employee entity.

        Request:
            {
                "username": "emp13",
                "first_name": "Employee",
                "last_name": "13",
                "email": "emp13@gateway.com",
                "mobile": "+917865594510",
                "is_active": true,
                "dob": "2002-12-12",
                "gender": "MALE"
            }

        Response:
            {
                "message": "Employee Details!",
                "success": true,
                "status": 200,
                "data": {
                    "id": 14,
                    "user": {
                        "pk": 102,
                        "username": "emp13",
                        "first_name": "Employee",
                        "last_name": "13",
                        "email": "emp13@gateway.com",
                        "mobile": "+917865594510",
                        "joined_date": "2022-03-11T14:23:27.300845+05:30",
                        "update_date": "2022-03-11T14:23:27.302828+05:30",
                        "is_active": true,
                        "is_staff": false
                    },
                    "interview_tech": null,
                    "created": "2022-03-11T14:23:27.303606+05:30",
                    "modified": "2022-03-11T14:23:27.304270+05:30"
                }
            }

        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(
            {
                'message': 'Employee Created Successfully!',
                'success': True,
                'status': status.HTTP_200_OK,
                'data': serializer.data
            }
        )

    def update(self, request, *args, **kwargs):
        """
        This method updates the particular employee details

        Request:
            {
                "employee_tech": 3
            }

        Response:
            {
                "message": "Employee details updated successfully",
                "success": true,
                "status": 200,
                "data": {
                    "id": 4,
                    "user": {
                        "pk": 91,
                        "username": "emp6",
                        "first_name": "Employee",
                        "last_name": "6",
                        "email": "emp6@gateway.com",
                        "mobile": "+918694652004",
                        "joined_date": "2022-03-11T11:04:12.281237+05:30",
                        "update_date": "2022-03-11T11:04:12.281475+05:30",
                        "is_active": true,
                        "is_staff": false
                    },
                    "interview_tech": {
                        "id": 3,
                        "technology_name": "Dot Net",
                        "is_active": false,
                        "created": "2022-01-03T18:52:09.620521+05:30",
                        "modified": "2022-01-03T18:52:09.620583+05:30"
                    },
                    "created": "2022-03-11T11:04:12.283029+05:30",
                    "modified": "2022-03-11T15:23:49.444667+05:30"
                }
            }


        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(
            {
                'message': 'Employee details updated successfully',
                'success': True,
                'status': status.HTTP_200_OK,
                'data': serializer.data
            }
        )


class EmployeeData(APIView):
    """
    Temporary API to get employee data (Delete this after ERP APIs integration)
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    http_method_names = [u'post']

    def post(self, request):
        # user = Employee.objects.get(user=self.request.user)
        # serializer = EmployeeSerializer(user)
        employee_id = request.data.get("employee_id")
        timestamp_data = request.data.get("timestamp_data")

        current_date = timezone.now().date()  # Get the current date
        time_parts = timestamp_data.split(":")
        hour, minute, second = map(int, time_parts)
        datetime_obj = datetime(current_date.year, current_date.month, current_date.day, hour, minute, second)

        time.sleep(1)
        employee = Employee.objects.get(employee_id=employee_id)
        employee_timestamp_obj = EmployeeDetectionTimeStamp.objects.create(
            employee=employee,
            timestamp=datetime_obj
        )
        time.sleep(1)
        return Response(
            {
                'message': 'Employee TimeStamp Data Added',
                'success': True,
                'status': status.HTTP_200_OK,
                'data': []
            }
        )


class EmployeeOutDataEntry(APIView):
    """
    Temporary API to get employee data (Delete this after ERP APIs integration)
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    http_method_names = [u'post']

    def post(self, request):
        # user = Employee.objects.get(user=self.request.user)
        # serializer = EmployeeSerializer(user)
        print("\n\n =========>>>>", request.data)
        employee_id = request.data.get("employee_id")
        timestamp_data = request.data.get("timestamp_data")

        current_date = timezone.now().date()  # Get the current date
        time_parts = timestamp_data.split(":")
        hour, minute, second = map(int, time_parts)
        datetime_obj = datetime(current_date.year, current_date.month, current_date.day, hour, minute, second)

        time.sleep(1)
        employee = Employee.objects.get(employee_id=employee_id)
        employee_timestamp_obj = EmployeeDetectionOutTimeStamp.objects.create(
            employee=employee,
            timestamp=datetime_obj
        )
        time.sleep(1)
        return Response(
            {
                'message': 'Employee Out TimeStamp Data Added',
                'success': True,
                'status': status.HTTP_200_OK,
                'data': []
            }
        )


class EmployeeDetectionTimestampViewset(viewsets.ModelViewSet):
    http_method_names = [u'get', u'post', u'put']
    serializer_class = EmployeeDetectionTimestampSerializer
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return EmployeeDetectionTimeStamp.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(
            {
                'message': 'Employee Detection Timestamp',
                'success': True,
                'status': status.HTTP_200_OK,
                'data': serializer.data
            }
        )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        return Response(
            {
                'message': 'Employee Detection Timestamp Details',
                'success': True,
                'status': status.HTTP_200_OK,
                'data': serializer.data
            }
        )

    def create(self, request, *args, **kwargs):
        """
        This method creates employee entity.

        Request:
            {
                "username": "emp13",
                "first_name": "Employee",
                "last_name": "13",
                "email": "emp13@gateway.com",
                "mobile": "+917865594510",
                "is_active": true,
                "dob": "2002-12-12",
                "gender": "MALE"
            }

        Response:
            {
                "message": "Employee Details!",
                "success": true,
                "status": 200,
                "data": {
                    "id": 14,
                    "user": {
                        "pk": 102,
                        "username": "emp13",
                        "first_name": "Employee",
                        "last_name": "13",
                        "email": "emp13@gateway.com",
                        "mobile": "+917865594510",
                        "joined_date": "2022-03-11T14:23:27.300845+05:30",
                        "update_date": "2022-03-11T14:23:27.302828+05:30",
                        "is_active": true,
                        "is_staff": false
                    },
                    "interview_tech": null,
                    "created": "2022-03-11T14:23:27.303606+05:30",
                    "modified": "2022-03-11T14:23:27.304270+05:30"
                }
            }

        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(
            {
                'message': 'Employee Detection Timestamp Added Successfully!',
                'success': True,
                'status': status.HTTP_200_OK,
                'data': serializer.data
            }
        )

    def update(self, request, *args, **kwargs):
        """
        This method updates the particular employee details

        Request:
            {
                "employee_tech": 3
            }

        Response:
            {
                "message": "Employee details updated successfully",
                "success": true,
                "status": 200,
                "data": {
                    "id": 4,
                    "user": {
                        "pk": 91,
                        "username": "emp6",
                        "first_name": "Employee",
                        "last_name": "6",
                        "email": "emp6@gateway.com",
                        "mobile": "+918694652004",
                        "joined_date": "2022-03-11T11:04:12.281237+05:30",
                        "update_date": "2022-03-11T11:04:12.281475+05:30",
                        "is_active": true,
                        "is_staff": false
                    },
                    "interview_tech": {
                        "id": 3,
                        "technology_name": "Dot Net",
                        "is_active": false,
                        "created": "2022-01-03T18:52:09.620521+05:30",
                        "modified": "2022-01-03T18:52:09.620583+05:30"
                    },
                    "created": "2022-03-11T11:04:12.283029+05:30",
                    "modified": "2022-03-11T15:23:49.444667+05:30"
                }
            }


        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(
            {
                'message': 'Employee Detection Timestamp Updated Successfully',
                'success': True,
                'status': status.HTTP_200_OK,
                'data': serializer.data
            }
        )


# class EmployeeSummaryGeneration(APIView):
#     http_method_names = [u'post']
#
#     def post(self, request):
#         employee_email = request.data.get('employee_email')
#         print("\n\n >>>>>>>>>>>>>>>>>.", employee_email)
#         punch_in_timestamps = EmployeeDetectionTimeStamp.objects.filter(
#             employee__user__email=employee_email
#         )
#         punch_out_timestamps = EmployeeDetectionOutTimeStamp.objects.filter(
#             employee__user__email=employee_email
#         )
#
#         total_working_hours = 0
#
#         # Iterate through pairs of punch-in and punch-out timestamps
#         for punch_in, punch_out in zip(punch_in_timestamps, punch_out_timestamps):
#             # Calculate the time duration between punch-in and punch-out
#             time_duration = punch_out.timestamp - punch_in.timestamp
#             # Convert the time duration to hours (you can adjust as needed)
#             hours_worked = time_duration.total_seconds() / 3600
#             # Add to the total working hours
#             total_working_hours += hours_worked
#
#         print("\n\n ******************", total_working_hours)
#         return Response(
#             {
#                 'message': 'Employee Summary Data',
#                 'success': True,
#                 'status': status.HTTP_200_OK,
#                 'data': []
#             }
#         )


class EmployeeSummaryGeneration(APIView):
    http_method_names = ['post']

    # def post(self, request):
    #     employee_email = request.data.get('employee_email')
    #     # month = request.data.get('month')
    #     month = request.data.get('month')
    #
    #     # Convert the 'month' string to a date object for filtering
    #     month_date = datetime.strptime(month, '%Y-%m')
    #
    #     # Retrieve punch-in and punch-out timestamps for the employee in the specified month
    #     punch_in_timestamps = EmployeeDetectionTimeStamp.objects.filter(
    #         employee__user__email=employee_email,
    #         timestamp__year=month_date.year,
    #         timestamp__month=month_date.month
    #     )
    #     punch_out_timestamps = EmployeeDetectionOutTimeStamp.objects.filter(
    #         employee__user__email=employee_email,
    #         timestamp__year=month_date.year,
    #         timestamp__month=month_date.month
    #     )
    #
    #     # Initialize variables for calculations
    #     total_working_hours = 0
    #     total_present_days = 0
    #     total_absent_days = 0
    #     total_overtime_hours = 0
    #
    #     # Define regular shift hours (9 hours)
    #     regular_shift_hours = 9
    #
    #     # Iterate through pairs of punch-in and punch-out timestamps
    #     for punch_in, punch_out in zip(punch_in_timestamps, punch_out_timestamps):
    #         # Calculate the time duration between punch-in and punch-out
    #         time_duration = punch_out.timestamp - punch_in.timestamp
    #         # Convert the time duration to hours
    #         hours_worked = time_duration.total_seconds() / 3600
    #
    #         # Check if the employee worked overtime
    #         if hours_worked > regular_shift_hours:
    #             overtime_hours = hours_worked - regular_shift_hours
    #             total_overtime_hours += overtime_hours
    #
    #         # Increment present days count
    #         total_present_days += 1
    #
    #         # Add hours worked to the total working hours
    #         total_working_hours += hours_worked
    #
    #     # Calculate total absent days
    #     total_days_in_month = month_date.replace(day=22)  # Assume max 28 days in a month
    #     print("\n\n ----->>>", type(total_days_in_month), total_days_in_month, type(total_present_days), total_present_days)
    #     total_days_in_month = month_date.replace(day=22)  # Assume max 28 days in a month
    #     total_absent_days = (total_days_in_month.day - total_present_days) if total_present_days <= 28 else 0
    #
    #     print("\n\n =>>>>>>>>>>>>>>>",
    #           {
    #               'employee_email': employee_email,
    #               'total_working_hours': total_working_hours,
    #               'total_present_days': total_present_days,
    #               'total_absent_days': total_absent_days,
    #               'total_overtime_hours': total_overtime_hours
    #           }
    #           )
    #
    #     return Response(
    #         {
    #             'message': 'Employee Summary Data',
    #             'success': True,
    #             'status': status.HTTP_200_OK,
    #             'data': {
    #                 'employee_email': employee_email,
    #                 'total_working_hours': total_working_hours,
    #                 'total_present_days': total_present_days,
    #                 'total_absent_days': total_absent_days,
    #                 'total_overtime_hours': total_overtime_hours
    #             }
    #         }
    #     )

    from django.db.models import Sum, F
    from django.db.models.functions import ExtractMonth
    from django.contrib.auth.models import User
    from django.http import Http404

    # def post(self, request):
    #     employee_email = request.data.get('employee_email')
    #     month = request.data.get('month')
    #
    #     if month:
    #         # Convert the 'month' string to a date object for filtering
    #         month_date = datetime.strptime(month, '%Y-%m')
    #
    #         # Retrieve punch-in and punch-out timestamps for the employee in the specified month
    #         punch_in_timestamps = EmployeeDetectionTimeStamp.objects.filter(
    #             employee__user__email=employee_email,
    #             timestamp__year=month_date.year,
    #             timestamp__month=month_date.month
    #         )
    #         punch_out_timestamps = EmployeeDetectionOutTimeStamp.objects.filter(
    #             employee__user__email=employee_email,
    #             timestamp__year=month_date.year,
    #             timestamp__month=month_date.month
    #         )
    #     else:
    #         # If 'month' is not provided, calculate data for the whole year
    #         year_date = datetime.now()  # Get the current year
    #         punch_in_timestamps = EmployeeDetectionTimeStamp.objects.filter(
    #             employee__user__email=employee_email,
    #             timestamp__year__gte=year_date.year,
    #         )
    #         punch_out_timestamps = EmployeeDetectionOutTimeStamp.objects.filter(
    #             employee__user__email=employee_email,
    #             timestamp__year__gte=year_date.year,
    #         )
    #
    #     if not punch_in_timestamps.exists() or not punch_out_timestamps.exists():
    #         raise Http404("Employee not found or no data for the specified month/year.")
    #
    #     # Initialize variables for calculations
    #     total_working_hours = 0
    #     total_present_days = 0
    #     total_absent_days = 0
    #     total_overtime_hours = 0
    #
    #     # Define regular shift hours (9 hours)
    #     regular_shift_hours = 9
    #
    #     # Iterate through pairs of punch-in and punch-out timestamps
    #     for punch_in, punch_out in zip(punch_in_timestamps, punch_out_timestamps):
    #         # Calculate the time duration between punch-in and punch-out
    #         time_duration = punch_out.timestamp - punch_in.timestamp
    #         # Convert the time duration to hours
    #         hours_worked = time_duration.total_seconds() / 3600
    #
    #         # Check if the employee worked overtime
    #         if hours_worked > regular_shift_hours:
    #             overtime_hours = hours_worked - regular_shift_hours
    #             total_overtime_hours += overtime_hours
    #
    #         # Increment present days count
    #         total_present_days += 1
    #
    #         # Add hours worked to the total working hours
    #         total_working_hours += hours_worked
    #
    #     # Calculate total absent days
    #     if month:
    #         # If 'month' is specified, calculate for the given month
    #         total_days_in_month = month_date.replace(day=28)  # Assume max 28 days in a month
    #         total_absent_days = (
    #                     total_days_in_month.day - total_present_days) if total_present_days <= 28 else 0
    #     else:
    #         # If 'month' is not specified, calculate for the whole year
    #         total_absent_days = 0
    #
    #     print("\n\n =>>>>>>>>>>>>>>>",
    #           {
    #               'employee_email': employee_email,
    #               'total_working_hours': total_working_hours,
    #               'total_present_days': total_present_days,
    #               'total_absent_days': total_absent_days,
    #               'total_overtime_hours': total_overtime_hours
    #           }
    #           )
    #
    #     return Response(
    #         {
    #             'message': 'Employee Summary Data',
    #             'success': True,
    #             'status': status.HTTP_200_OK,
    #             'data': {
    #                 'employee_email': employee_email,
    #                 'total_working_hours': total_working_hours,
    #                 'total_present_days': total_present_days,
    #                 'total_absent_days': total_absent_days,
    #                 'total_overtime_hours': total_overtime_hours
    #             }
    #         }
    #     )

    def post(self, request):
        employee_email = request.data.get('employee_email')
        # month = request.data.get('month')
        month = "2023-10"

        # Convert the 'month' string to a date object for filtering
        month_date = datetime.strptime(month, '%Y-%m')

        # Retrieve punch-in and punch-out timestamps for the employee in the specified month
        punch_in_timestamps = EmployeeDetectionTimeStamp.objects.filter(
            employee__user__email=employee_email,
            timestamp__year=month_date.year,
            timestamp__month=month_date.month
        )
        punch_out_timestamps = EmployeeDetectionOutTimeStamp.objects.filter(
            employee__user__email=employee_email,
            timestamp__year=month_date.year,
            timestamp__month=month_date.month
        )

        # Initialize variables for calculations
        total_working_hours = 0
        total_present_days = 0
        total_absent_days = 0
        total_overtime_hours = 0

        # Define regular shift hours (9 hours)
        regular_shift_hours = 9

        # Iterate through pairs of punch-in and punch-out timestamps
        for punch_in, punch_out in zip(punch_in_timestamps, punch_out_timestamps):
            # Calculate the time duration between punch-in and punch-out
            time_duration = punch_out.timestamp - punch_in.timestamp
            # Convert the time duration to hours
            hours_worked = time_duration.total_seconds() / 3600

            # Check if the employee worked overtime
            if hours_worked > regular_shift_hours:
                overtime_hours = hours_worked - regular_shift_hours
                total_overtime_hours += overtime_hours

            # Increment present days count
            total_present_days += 1

            # Add hours worked to the total working hours
            total_working_hours += hours_worked

        # Calculate total absent days
        total_days_in_month = month_date.replace(day=22)  # Assume max 28 days in a month
        total_days_in_month = month_date.replace(day=22)  # Assume max 28 days in a month
        total_absent_days = (total_days_in_month.day - total_present_days) if total_present_days <= 28 else 0

        return Response(
            {
                'message': 'Employee Summary Data',
                'success': True,
                'status': status.HTTP_200_OK,
                'data': {
                    'employee_email': employee_email,
                    'total_working_hours': round(total_working_hours, 2),
                    'total_present_days': total_present_days,
                    'total_absent_days': total_absent_days,
                    'total_overtime_hours': round(total_overtime_hours, 2),
                    'sample_data1': [100, 100, 90, 85, 92, 98, 100, 90, 95, 100, 90],
                    'sample_data2': [44, 55, 41, 67, 22, 43, 21, 41, 56, 27, 43],
                    'sample_data3': [90, 90, 70, 74, 90, 80, 92, 80, 90, 95, 100],
                    'demo_data1': [80, 50, 30, 40, 100],
                    'demo_data2': [20, 30, 40, 80, 20],
                    'demo_data3': [44, 76, 78, 13, 43]
                }
            }
        )