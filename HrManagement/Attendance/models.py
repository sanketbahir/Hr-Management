from django.db import models
from employee.models import Employee

# Create your models here.
class Attendance(models.Model):
    STATUS_CHOICES = [ 
        ('present', 'Present'), 
        ('absent', 'Absent'),
        ('on_leave', 'On Leave'),
    ]
    # employee = models.CharField(max_length=50)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)     
    date_of_attendance = models.DateField() 
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)