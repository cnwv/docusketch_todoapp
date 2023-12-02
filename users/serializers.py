from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from .models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
