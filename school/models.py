from django.db import models

from Home.models import User

# Create your models here.

class School(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)