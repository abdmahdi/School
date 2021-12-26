from django.contrib import admin
from Home.models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_filter = ["is_teacher","is_student","is_school"]
    
 

admin.site.register(User,UserAdmin)
admin.site.register(Wilaya)
admin.site.register(Days)
admin.site.register(Matier)

admin.site.register(Level)
admin.site.register(Division)
admin.site.register(Annee)