from django.contrib import admin
from student.models import *

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ["first_name","last_name","email"]
    list_filter = ["wilaya","matier"]
 
    
admin.site.register(Student,StudentAdmin)