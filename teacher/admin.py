from django.contrib import admin

from teacher.models import PostTeacher, Teacher , Groupe

# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["first_name","last_name","email"]
    list_filter = ["wilaya","matier",'level']
 
class TeacherPostAdmin(admin.ModelAdmin):
    list_display = ["teacher","title","slug","created"]
    list_filter = ["matier",'level',"division"]
    
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(PostTeacher,TeacherPostAdmin)
admin.site.register(Groupe)