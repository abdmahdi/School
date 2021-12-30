from django.db import models
from Home.models import *


# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    email = models.EmailField(unique=True,null=True)
    phone = models.IntegerField(null=True)
    wilaya = models.ForeignKey(Wilaya, on_delete=models.DO_NOTHING,null=True,unique=False)
    pic = models.ImageField(null=True, blank=True, upload_to="images", default="user.png")
    level = models.ForeignKey(Level, on_delete=models.DO_NOTHING,null=True,unique=False)
    division = models.ForeignKey(Division, on_delete=models.DO_NOTHING,null=True,unique=False)
    annee = models.ForeignKey(Annee, on_delete=models.DO_NOTHING,null=True,unique=False)
    matier = models.ManyToManyField(Matier, related_name='preferer',unique=False)
    
    def __str__(self):
        return f"Mr. {self.first_name}   {self.last_name}   "