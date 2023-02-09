from django.db import models

# Create your models here.
class login_db(models.Model):
    Name = models.CharField(max_length=30, null=True, blank=True)
    Email = models.CharField(max_length=30, null=True, blank=True)
    Password = models.CharField(max_length=30, null=True, blank=True)
    Cpassword = models.CharField(max_length=30, null=True, blank=True)

class contact(models.Model):
    Name = models.CharField(max_length=30, null=True, blank=True)
    Email = models.CharField(max_length=50, null=True, blank=True)
    Subject = models.CharField(max_length=50, null=True, blank=True)
    Message = models.CharField(max_length=300,null=True, blank=True)