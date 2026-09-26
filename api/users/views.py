from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from api.users.serializers import UserSerializer, UpdateProfileSerializer, LoginSerializer, RegisterSerializer
from user_module.models import User


class ProfileAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserSerializer

        return UpdateProfileSerializer

    def get_object(self):
        return self.request.user


class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer


class LoginAPIView(TokenObtainPairView):
    serializer_class = LoginSerializer