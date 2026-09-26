from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from user_module.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
        ]


class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
        ]

    def validate_email(self, value):
        user = self.instance

        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError('این ایمیل قبلا ثبت شده')

        return value

    def validate_username(self, value):
        user = self.instance

        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError('این نام کاربری قبلا ثبت شده')

        return value


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "confirm_password",
        ]

        read_only_fields = [
            "id",
        ]

    def validate(self, attrs):
        password = attrs["password"]
        confirm_password = attrs["confirm_password"]

        if password != confirm_password:
            raise serializers.ValidationError(
                {
                    "password": "password and confirmation password do not match",
                }
            )

        return attrs

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data["user"] = UserSerializer(self.user).data

        return data