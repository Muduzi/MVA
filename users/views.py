from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from .models import Profile
from .serializer import ProfileSerializer, RegisterSerializer, LoginSerializer, UserSerializer

# Create your views here.


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    
    def put(self, request, *args, **kwargs):
        profile = Profile.objects.get(User__id=request.user.id)
        serializer = ProfileSerializer(profile, data=request.data, partial=False)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        print(f'request.data : {request.data}')
        profile = request.user.profile
        photo = request.FILES.get('Photo')

        serializer = ProfileSerializer(profile, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save(Photo=request.FILES.get('Photo'))
            serializer.save()
            print(f'profile =========================', request.FILES.get('Photo'))
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # print(f'profile error ========================== {serializer.errors}')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        try:
            profile = request.user.profile
            serializer = ProfileSerializer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
            return Response({'error': "Profile not found"}, status=status.HTTP_404_NOT_FOUND)


class RegisterUser(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors)


class LoginUSer(TokenObtainPairView):
    serializer_class = LoginSerializer


class UserDetails(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=False)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        # print(f'request.data1++++++++++++++++++++++++++++++++++++++++++++++=={request.data}')
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            # print(f'user ========================={serializer.data}')
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        try:
            user = request.user
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'user does not exist'}, status=status.HTTP_404_NOT_FOUND)



