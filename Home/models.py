from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(('email address'), unique=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_school = models.BooleanField(default=False)
    bio = models.TextField(null=True)
    


class Wilaya(models.Model):
    wilaya = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=5)
    
    def __str__(self):
        return f"{self.wilaya}  \n   ({self.zip_code})"



class Matier(models.Model):
    Matier =  models.CharField(max_length=50)
    
    def __str__(self):
	    return self.Matier
 
 
 
 
class Days(models.Model):
    day = models.CharField(max_length=20) 
    def __str__(self):
         return self.day




class Division(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name 
 
class Annee(models.Model):
    annee = models.CharField(blank=False,max_length=10,null=False)
    def __str__(self):
        return self.annee 
    
class Level(models.Model):
    level = models.CharField(max_length=20)
   
    def __str__(self):
        return self.level 
    




    