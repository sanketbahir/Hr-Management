from rest_framework import serializers
from .models import Employee
from department.serializers import DepartmentSerializer

class EmployeeSerializer(serializers.ModelSerializer):
    department_id = serializers.IntegerField(write_only=True)
    department = DepartmentSerializer(read_only=True) 
    
    class Meta:
        model = Employee
        fields= ['id','first_name','last_name','email','phone_number','designation','gender','profile_pic','data_of_joining','status','department_id','department']
        read_only_fields =['id']


