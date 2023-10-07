from rest_framework.response import Response
from rest_framework import viewsets, authentication,permissions, status
from rest_framework.views import APIView

from .serializers import EmployeeSerializer
from .models import Employee


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
        return Response(
            {
                'message': 'Employee Data',
                'success': True,
                'status': status.HTTP_200_OK,
                'data': []
            }
        )
