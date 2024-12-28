from django.db import models
<<<<<<< HEAD
from employee.models import Employee
=======
# from employee.models import Employee
>>>>>>> fd6d0b8c5e27194f5f4161022f1ccf50c9d23821

# Create your models here.
class Attendance(models.Model):
    STATUS_CHOICES = [ 
        ('present', 'Present'), 
        ('absent', 'Absent'),
        ('on_leave', 'On Leave'),
    ]
<<<<<<< HEAD
    # employee = models.CharField(max_length=50)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)     
=======
    employee = models.CharField(max_length=50)
    # employee = models.ForeignKey(Employee, on_delete=models.CASCADE)     
>>>>>>> fd6d0b8c5e27194f5f4161022f1ccf50c9d23821
    date_of_attendance = models.DateField() 
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)