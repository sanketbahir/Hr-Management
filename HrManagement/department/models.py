from django.db import models
<<<<<<< HEAD
=======
# from employee.models import Employee
>>>>>>> fd6d0b8c5e27194f5f4161022f1ccf50c9d23821

# Create your models here.
class Department(models.Model):
    department_name = models.CharField(max_length=100)
<<<<<<< HEAD
    # head =  models.CharField(max_length=50)  
=======
    head =  models.CharField(max_length=50)  
>>>>>>> fd6d0b8c5e27194f5f4161022f1ccf50c9d23821
    # head = models.ForeignKey('employee.Employee', related_name='departments_headed', on_delete=models.CASCADE) 
    description = models.TextField()

