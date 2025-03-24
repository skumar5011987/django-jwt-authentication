from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
 
class RegisterAPIView(generics.CreateAPIView):
    users = User.objects.all()
    permission_calsses = (AllowAny,)
    serializer_class = RegisterSerializer

class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user=user)
            user_serializer = UserSerializer(user)

            return Response({
                "user": user_serializer.data,
                "refresh_token": str(refresh),
                "access_token": str(refresh.access_token)
            })
        
        return Response({
            "error":"Invalid Login Credentials."
        }, status=401)


class HomeAPIView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        user_serializer = UserSerializer(user)

        return Response({
            "message": "Welcome, Django JWT working well.",
            "user": user_serializer.data
        }, status=200)
