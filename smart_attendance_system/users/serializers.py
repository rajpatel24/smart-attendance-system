from django.db import transaction
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_auth import serializers as auth_serializers
from rest_auth.models import TokenModel

User = get_user_model()


class UserDetailsSerializer(auth_serializers.UserDetailsSerializer):
    """
    User Details Serializer
    """

    class Meta:
        model = User
        fields = ('pk', 'username',
                  'first_name', 'last_name',
                  'email', 'mobile',
                  'joined_date', 'update_date',
                  'is_active', 'is_staff')
        read_only_fields = ('username',)
        ref_name = 'User'

    def update(self, instance, validated_data):
        super().update(instance, validated_data)
