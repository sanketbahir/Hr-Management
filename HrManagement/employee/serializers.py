from rest_framework import serializers
from .models import Employee
from user.models import CustomUser
from rest_framework.validators import UniqueValidator

class EmployeeSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Employee.objects.all())]
    )
    phone_number = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=Employee.objects.all())]
    )
    department = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.filter(role='Admin'),
        required=True
    )

    class Meta:
        model = Employee
        fields = [
            'id', 'first_name', 'last_name', 'email', 'phone_number', 'department', 
            'designation', 'gender', 'profile_pic', 'date_of_joining', 'status'
        ]

    def validate_gender(self, value):

        if value not in dict(Employee.GENDER_CHOICES):
            raise serializers.ValidationError("Invalid gender. Must be 'Male', 'Female', or 'Other'.")
        return value

    def validate_status(self, value):
        if value not in dict(Employee.STATUS_CHOICES):
            raise serializers.ValidationError("Invalid status. Must be 'Active' or 'Inactive'.")
        return value

    def validate(self, attrs):
        if not attrs['first_name'].strip() or not attrs['last_name'].strip():
            raise serializers.ValidationError({"name": "First name and last name cannot be empty or whitespace."})
        return attrs
