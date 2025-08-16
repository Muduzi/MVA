from rest_framework import serializers
from rest_framework_simplejwt.tokens import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Profile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, AuthUser
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        data['firstname'] = self.user.first_name
        data['lastname'] = self.user.last_name
        data['email'] = self.user.email
        data['id'] = self.user.id
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id']


class ProfileSerializer(serializers.ModelSerializer):
    # nested serializer to represent
    # user details(optional, for read operations)

    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ['id', 'Date']


"""    user = UserSerializer(read_only=True)

    # use PrimaryKeyRelatedField for write operations (to accept user id)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True
    )
"""



