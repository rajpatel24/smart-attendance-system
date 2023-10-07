from django.db import transaction
from django.shortcuts import get_object_or_404

from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

from users.models import User
from users.serializers import UserDetailsSerializer

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserDetailsSerializer(read_only=True)
    employee_id = serializers.IntegerField(write_only=True, required=True)
    username = serializers.CharField(required=False, write_only=True)
    first_name = serializers.CharField(required=False, write_only=True)
    last_name = serializers.CharField(required=False, write_only=True)
    email = serializers.EmailField(required=False, write_only=True)
    mobile = PhoneNumberField(required=False, write_only=True)
    is_active = serializers.BooleanField(required=False, write_only=True)

    class Meta:
        model = Employee
        fields = (
            'id', 'user', 'created', 'modified', 'username',
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
