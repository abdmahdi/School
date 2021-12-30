from django.contrib import admin

from school.models import *

# Register your models here.
class SchoolAdmin(admin.ModelAdmin):
    list_display = ["first_name","last_name","email"]
    list_filter = ["wilaya","matier",'level']
 
class SchoolPostAdmin(admin.ModelAdmin):
    list_display = ["school","title","slug","created"]
    list_filter = ["matier",'level',"division"]
    
admin.site.register(School,SchoolAdmin)
admin.site.register(PostSchool,SchoolPostAdmin)
admin.site.register(GroupeSchool)