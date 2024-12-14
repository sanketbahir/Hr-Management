from django.db import models

# Create your models here.
class Attendance(models.Model):
    STATUS_CHOICES = [ 
        ('present', 'Present'), 
        ('absent', 'Absent'), 
        ('on_leave', 'On Leave'),
    ]
    employee_name = models.CharField( max_length=50) 
    date_of_attendance = models.DateField() 
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)