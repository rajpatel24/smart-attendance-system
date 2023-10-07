from django.db import transaction
from django.shortcuts import get_object_or_404

from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

from django.utils import timezone
from datetime import datetime

from users.models import User
from users.serializers import UserDetailsSerializer

from .models import Employee, EmployeeDetectionTimeStamp


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserDetailsSerializer(read_only=True)
    username = serializers.CharField(required=False, write_only=True)
    first_name = serializers.CharField(required=False, write_only=True)
    last_name = serializers.CharField(required=False, write_only=True)
    email = serializers.EmailField(required=False, write_only=True)
    mobile = PhoneNumberField(required=False, write_only=True)
    is_active = serializers.BooleanField(required=False, write_only=True)

    class Meta:
        model = Employee
        fields = (
            'id', 'employee_id', 'user', 'created', 'modified', 'username',
            'first_name', 'last_name', 'email', 'employee_id',
            'is_active', 'mobile',
        )

    def create(self, validated_data):
        with transaction.atomic():
            employee_id = validated_data['employee_id']
            first_name = validated_data['first_name']
            last_name = validated_data['last_name']
            email = validated_data['email']
            mobile = validated_data['mobile']
            is_active = validated_data['is_active']

            user_obj = User.objects.filter(mobile=mobile, email=email)

            if not user_obj:
                new_user = User.objects.create(first_name=first_name,
                                               last_name=last_name,
                                               email=email,
                                               mobile=mobile,
                                               is_active=is_active
                                               )
                new_user.save()

                new_emp = Employee.objects.create(user=new_user,
                                                  employee_id=employee_id,
                                                  )
                new_emp.save()
                return new_emp

            else:
                return '{}'

    def update(self, instance, validated_data):
        with transaction.atomic():
            first_name = validated_data.get('first_name', instance.user.first_name)
            last_name = validated_data.get('last_name', instance.user.last_name)
            email = validated_data.get('email', instance.user.email)
            mobile = validated_data.get('mobile', instance.user.mobile)
            is_active = validated_data.get('is_active', instance.user.is_active)

            # Update user details
            instance.user.first_name = first_name
            instance.user.last_name = last_name
            instance.user.email = email
            instance.user.mobile = mobile
            instance.user.is_active = is_active
            instance.user.save()

            instance.save()

        return instance


class EmployeeDetectionTimestampSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    timestamp_data = serializers.CharField(write_only=True)
    employee_id = serializers.IntegerField(write_only=True, required=True)
    username = serializers.CharField(required=False, write_only=True)

    class Meta:
        model = EmployeeDetectionTimeStamp
        fields = (
            'id', 'timestamp', 'employee', 'employee_id', 'username', 'created', 'modified', 'username', 'timestamp_data'
        )

    def create(self, validated_data):
        with transaction.atomic():
            employee_id = validated_data['employee_id']
            timestamp = validated_data['timestamp_data']

            current_date = timezone.now().date()  # Get the current date
            time_parts = timestamp.split(":")
            hour, minute, second = map(int, time_parts)
            datetime_obj = datetime(current_date.year, current_date.month, current_date.day, hour, minute, second)

            employee = Employee.objects.get(employee_id=employee_id)

            employee_timestamp_obj = EmployeeDetectionTimeStamp.objects.create(
                employee=employee,
                timestamp=datetime_obj
            )

            employee_timestamp_obj.save()
            return employee_timestamp_obj

    def update(self, instance, validated_data):
        with transaction.atomic():
            timestamp = validated_data['timestamp_data']

            current_date = timezone.now().date()  # Get the current date
            time_parts = timestamp.split(":")
            hour, minute, second = map(int, time_parts)
            datetime_obj = datetime(current_date.year, current_date.month, current_date.day, hour, minute, second)

            instance.timestamp = datetime_obj
            instance.save()
        return instance
