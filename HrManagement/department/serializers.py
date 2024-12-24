from rest_framework import serializers
from .models import Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields="__all__"
        read_only_fields =['id']

# class DepartmentDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Department
#         fields = DepartmentSerializer.Meta.fields
#         read_only_fields =['id']


# class DepartmentImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Department
#         fields = ['id',]
#         read_only_fields =['id']

