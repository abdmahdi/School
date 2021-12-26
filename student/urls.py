from django.urls import path
from student.views import *
urlpatterns = [
    path('', homestudent, name="HomeStudent"),
    path('register/',StudentSignUpView.as_view(), name="registerStudent"),
     path('login/', loginPage, name='loginStudent'),
    path('post/<slug:slug>/', post, name="post"),

    # path('profile/',views.updateProfile, name="Profile")
]
