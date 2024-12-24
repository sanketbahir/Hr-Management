from django.db import models

# Create your models here.
class Department(models.Model):
    department_name = models.CharField(max_length=100)
    # head =  models.CharField(max_length=50)  
    # head = models.ForeignKey('employee.Employee', related_name='departments_headed', on_delete=models.CASCADE) 
    description = models.TextField()

