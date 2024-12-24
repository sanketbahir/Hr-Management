from rest_framework import serializers
from .models import Attendance
from employee.serializers import EmployeeSerializer

class AttendanceSerializer(serializers.ModelSerializer):
    employee_id = serializers.IntegerField(write_only=True)
    employee = EmployeeSerializer(read_only=True) 

    class Meta:
        model = Attendance
        fields= ['id','date_of_attendance','status','employee_id','employee']
        read_only_fields =['id']