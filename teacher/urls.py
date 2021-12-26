from django.urls import path
from teacher.views import *
urlpatterns = [
    path('', hometeacher, name="HomeTeacher"),
    path('register/',TeacherSignUpView.as_view(), name='registerTeacher'),
    path('login/',LoginTeacher, name='loginTeacher'),
    path('createpost/',createPost, name='createPost'),
    path('groups/', creategroup, name='Groups'),
    path('update_post/<slug:slug>/', updatePost, name="update_post"),
	path('delete_post/<slug:slug>/', deletePost, name="delete_post"),

]
