from rest_framework import serializers
from .models import Attendance
<<<<<<< HEAD
from employee.serializers import EmployeeSerializer

class AttendanceSerializer(serializers.ModelSerializer):
    employee_id = serializers.IntegerField(write_only=True)
    employee = EmployeeSerializer(read_only=True) 

    class Meta:
        model = Attendance
        fields= ['id','date_of_attendance','status','employee_id','employee']
=======


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields="__all__"
>>>>>>> fd6d0b8c5e27194f5f4161022f1ccf50c9d23821
        read_only_fields =['id']