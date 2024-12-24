from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):  # Inherit from AbstractUser
    ROLE_CHOICES = [
        ('Admin', 'admin'),
        ('Employee', 'employee'),
    ]
    # Optional: You can customize these fields as needed
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='Employee')
    # If you want to add custom fields like profile_picture, department, etc., you can do so here.
    # You don't need 'password' or 'date_joined' as they are already provided by AbstractUser

    # If you want to override any default behavior, you can do so here
    # For example, you could add custom save behavior or methods.
