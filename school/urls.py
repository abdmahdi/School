from django.urls import path
from school.views import *
urlpatterns = [
    path('', homeSchool, name="HomeSchool"),
    path('register/',SchoolSignUpView.as_view(), name='registerSchool'),
    path('login/',LoginSchool, name='loginSchool'),
    path('logout/', logoutUser, name='logoutSchool'),
    path('Posts/', postsSchool, name='PostsSchool'),
    path('createpost/',createPost, name='createPost'),
    path('account/', SchoolAccount, name="SchoolAccount"),
    path('update_profile/', updateProfileSchool, name="update_profileSchool"),
    path('groups/<slug:slug>/', creategroup, name='Groups'),
    path('postView/<slug:slug>/', post, name="schoolpost"),
    path('update_post/<slug:slug>/', updatePost, name="update_post"),
	path('delete_post/<slug:slug>/', deletePost, name="delete_post"),

]
