from django.db import models
from user.models import CustomUser  # Import the CustomUser model

def employee_profile_image_file(instance, filename):
    return '/'.join(['employee_images', str(instance.id), filename])

class Employee(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]

    ACTIVE = 'Active'
    INACTIVE = 'Inactive'
    STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    department = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='employees')
    designation = models.CharField(max_length=100)
    profile_pic = models.ImageField(
        upload_to=employee_profile_image_file, 
        blank=True, 
        null=True
    )
    date_of_joining = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=ACTIVE)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.designation})"
