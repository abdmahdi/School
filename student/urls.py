from django.urls import path
from student.views import *
urlpatterns = [
    #Home Student
    path('', homestudent, name="HomeStudent"),
    #POsts :: Post
    path('posts/', posts, name="Posts"),
    path('post/<slug:slug>/', post, name="post"),
    
    # Sign UP Student
    path('register/',StudentSignUpView.as_view(), name="registerStudent"),
    # profile student
    path('account/', StudentAccount, name="StudentAccount"),
    path('update_profile/', updateProfile, name="update_profileStudent"),
    
    
    #login/// logout
    path('login/', loginPage, name='loginStudent'),
    path('logout/', logoutUser, name='logoutStudent'),
   


    
]

