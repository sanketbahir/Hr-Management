from django.db import models
from department.models import Department

# Create your models here.
class Employee(models.Model):
    GENDER_CHOICES = [ 
        ('Male', 'Male'), 
        ('female', 'female'),
        ('other', 'other'),
    ]
    STATUS_CHOICES = [ 
        ('active', 'active'),
        ('inactive', 'active'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    # department =models.CharField(max_length=50)
    department = models.ForeignKey('department.Department', on_delete=models.CASCADE)  
    designation = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    profile_pic = models.ImageField(models.ImageField(upload_to='profile_pics/', null=True))
    data_of_joining = models.DateField() 
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)   
    