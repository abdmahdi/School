from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from Home.models import *

# Create your models here.

class School(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
   school_name = models.CharField(max_length=200, unique=True, null=True)
   first_name = models.CharField(max_length=200, blank=True, null=True)
   last_name = models.CharField(max_length=200, blank=True, null=True)
   email = models.CharField(max_length=200,unique=True,null=True)
   wilaya = models.ForeignKey(Wilaya, on_delete=models.DO_NOTHING, default=None)
   adress = models.CharField(max_length=200, default=None)
   pic = models.ImageField(null=True, blank=True, upload_to="images", default="school.png")
   phone = models.IntegerField(null = True)
   level = models.ForeignKey(Level, blank=False, null=False, on_delete=models.DO_NOTHING,default=None)
   matier = models.ManyToManyField(Matier)
   bio = models.TextField(null=True, blank=True)
   def __str__(self):
        return f"{self.school_name}"
     
     

class PostSchool(models.Model):
   school = models.ForeignKey(School, on_delete=models.CASCADE,null=True)
   title = models.CharField(max_length=200)
   image =  models.ImageField(null=True, blank=True, upload_to="images", default="placeholder.png")
   body = RichTextUploadingField(null=True, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   active = models.BooleanField(default=False)
   matier = models.ForeignKey(Matier,null=False,blank=False,on_delete=models.DO_NOTHING)
   level = models.ForeignKey(Level, null=False, blank=False,on_delete=models.DO_NOTHING)
   division = models.ForeignKey(Division, null=True, blank=True, on_delete=models.DO_NOTHING)
   Annee = models.ForeignKey(Annee, null=False, blank=False, on_delete=models.DO_NOTHING,default=None) 
   slug = models.SlugField(null=True, blank=True)
   
   def __str__(self):
       return self.title 
   
   def save(self, *args, **kwargs):
       if self.slug == None:
           slug = slugify(self.title)
           has_slug = PostSchool.objects.filter(slug=slug).exists()
           count = 1
           while has_slug:
               count+=1
               slug = slugify(self.title)+ '-' + str(count)
               has_slug = PostSchool.objects.filter(slug=slug).exists()
               
           self.slug = slug     
        
       super().save(*args, **kwargs)   


class GroupeSchool(models.Model):
    postschool = models.ForeignKey(PostSchool,on_delete=models.CASCADE ,null=True)
    N_groupe = models.IntegerField()
    Days = models.ForeignKey(Days, on_delete=models.DO_NOTHING)
    starttime = models.TimeField()
    endstime = models.TimeField()    
    nombredeplace = models.IntegerField(default=None)
    
    def __str__(self):
        return f"{self.Days} /// start at : {self.starttime} ends at {self.endstime} "     