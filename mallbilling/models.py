from django.db import models
from django.contrib.auth.models import AbstractUser
from django.http import JsonResponse



class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name






class Admin(models.Model):
    admin_id = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    # Add any other fields you need for the admin

    def __str__(self):
        return self.admin_id

class Employee(models.Model):
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    employee_id = models.EmailField(unique=True, null=True)
    password = models.CharField(max_length=128)
    USERNAME_FIELD = 'employee_id'
    # REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.employee_id

    # Add any other fields you need for the employee

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # Add any other fields you need for the product

    def __str__(self):
        return self.name
