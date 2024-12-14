from django.db import models
# from employee.models import Employee

# Create your models here.
class Department(models.Model):
    department_name = models.CharField(max_length=100)
    head =  models.CharField(max_length=50)#models.ForeignKey(Employee,on_delete=models.CASCADE)  
    description = models.TextField()

