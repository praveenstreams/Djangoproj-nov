from django.db import models

# Create your models here.
class student_model(models.Model):
    name=models.CharField(max_length=100)
    dob=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

class admin_model(models.Model):
    name = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)