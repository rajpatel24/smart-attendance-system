import uuid

import requests
from django.core.files.uploadedfile import SimpleUploadedFile
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

import base64
from django.core.files.base import ContentFile

from employees.models import Employee
from .models import User


# Create your views here.


class RegistrationAPIView(APIView):
    http_method_names = [u'post']

    def post(self, request):
        body = {
            'username': request.data['email'],
            # 'email': request.data['email'],
            # 'mobile': request.data['mobile'],
            'password1': request.data['password2'],
            'password2': request.data['password2']
        }

        response = requests.post(
            'http://127.0.0.1:8000/api/v1/rest-auth/registration/',
            json=body
        )
        print("\n\n ************", request.data, request.data['email'])

        if response.status_code == status.HTTP_201_CREATED:
            user = User.objects.get(username=request.data['email'])
            user.first_name = request.data['first_name']
            user.last_name = request.data['last_name']
            user.email = request.data['email']
            user.mobile = request.data['mobile']
            user.save()

            base64_img = request.data['photo']
            image_data = base64_img.split(';base64,')[1]
            image_binary = base64.b64decode(image_data)
            image_file = ContentFile(image_binary)
            image_upload = SimpleUploadedFile(f'{uuid.uuid4()}.jpg', image_file.read())

            employee = Employee.objects.create(
                user=user,
                employee_id=request.data['emp_id'],
                employee_image1=image_upload
            )

            return Response(
                {
                    'message': 'User registered successfully',
                    'success': True,
                    'status': status.HTTP_200_OK
                },
                status=status.HTTP_200_OK
            )
        else:
            print("\n\n ============>>>>>>>", response)
            error_message = response.json().get('error_message', 'Unknown error')
            return Response(
                {
                    'message': 'Registration failed',
                    'error_message': error_message,
                    'success': False,
                    'status': response.status_code
                },
                status=response.status_code
            )
