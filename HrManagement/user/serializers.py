from rest_framework import serializers
from .models import CustomUser
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role', 'is_active', 'date_joined', 'last_login']
        extra_kwargs = {
            'is_active': {'read_only': True},
            'date_joined': {'read_only': True},
            'last_login': {'read_only': True},
        }


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True
    )
    role = serializers.ChoiceField(
        choices=[('Admin', 'Admin'), ('Employee', 'Employee')],
        required=True
    )
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    # Make these fields visible in the Swagger UI
    is_active = serializers.BooleanField(
        required=False,
        default=True
    )
    date_joined = serializers.DateTimeField(
        read_only=True,
        default=True
    )
    last_login = serializers.DateTimeField(
        read_only=True,
        default=True
    )

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'password2', 'role', 'is_active', 'date_joined', 'last_login']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            role=validated_data['role'],
            is_active=validated_data.get('is_active', True)  # Default value if not provided
        )
        user.set_password(validated_data['password'])  # Hashes the password
        user.save()
        return user
