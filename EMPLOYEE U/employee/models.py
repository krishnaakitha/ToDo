from django.db import models

# Create your models here.

class Employee(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Photo = models.ImageField(upload_to='images')
    Designation = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100,unique=True)
    Phone_Number = models.CharField(max_length=12,blank=True)
    Created_at = models.DateTimeField(auto_now_add=True)
    Upload_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.First_Name