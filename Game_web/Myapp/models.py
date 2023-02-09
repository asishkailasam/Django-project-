from django.db import models

# Create your models here.
class Game_admindb(models.Model):
    uname =models.CharField(max_length=100, null=True, blank=True)
    email =models.EmailField(null=True, blank=True)
    image  = models.ImageField(upload_to="profile", null=True ,blank =True)
    password = models.CharField(max_length=100, null=True, blank=True)
    cpassword = models.CharField(max_length=100, null=True, blank=True)

class Game_catdb(models.Model):
    cname=models.CharField(max_length=100, null=True, blank=True)
    info=models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to="profile", null=True, blank=True)


class Game_prodb(models.Model):
    cname =models.CharField(max_length=100, null=True, blank=True)
    pname = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    info=models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to="profile", null=True, blank=True)
