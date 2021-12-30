from django.shortcuts import redirect, render
from django.contrib.auth.models import Group, User,auth
from django.contrib.auth import login
from django.views.generic import *
from student.forms import *
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from student.decorators import *
from teacher.models import PostTeacher
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from student.filters import *
from school.models import *

@student_required
def homestudent(request):
    return render(request, 'student/HomeStudent.html')
    

# Create your views here.
@student_required
def posts(request):
	posts = PostTeacher.objects.filter(active=True)
	myFilter = PostFilter(request.GET, queryset=posts)
	posts = myFilter.qs

	page = request.GET.get('page')

	paginator = Paginator(posts, 5)

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	context = {'posts':posts, 'myFilter':myFilter}
	return render(request, 'student/posts.html', context)

@student_required
def postschool(request):
    postss = PostSchool.objects.filter(active=True)
    Filterschool = PostFilterSchool(request.GET, queryset=postss)
    postss=Filterschool.qs
    page = request.GET.get('page')
    paginator = Paginator(postss, 5)
    try:
        
        postss = paginator.page(page)
    except PageNotAnInteger:
       
        postss = paginator.page(1)
    except EmptyPage:
       
        postss = paginator.page(paginator.num_pages)
    
    context = {'postschool':postss, 'filterschool':Filterschool}  
    return render(request, 'student/postschool.html', context)      
    
    

# @student_required
# def post(request, slug):
# 	post = PostTeacher.objects.get(slug=slug)
#     group = Groupe.objects.get(postteacher = post)
# 	context = {'post':post, 'group':group}
# 	return render(request, 'student/post.html', context)

    
@student_required
def post(request,slug):
    post = PostTeacher.objects.get(slug=slug)
    groups = Groupe.objects.filter(postteacher = post)
    posts = PostSchool.objects.get(slug=slug)
    groupss = GroupeSchool.objects.filter(postschool = posts)
    context = {'post':post, 'groups':groups, 'postschool':posts, 'groupschool':groupss}
    return render(request, 'student/post.html', context)


              
class StudentSignUpView(CreateView):
    model = User
    form_class = UserSignUp
    template_name = 'student/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('loginStudent')
    


def active(request):
        request.user.is_active=True
        
def loginPage(request):
    
	if request.user.is_authenticated and request.user.is_student==True:
		return redirect('HomeStudent')
	if request.method == 'POST':
		email = request.POST.get('email')
		password =request.POST.get('password')
		try:
			user = User.objects.get(email=email)
			user = authenticate(request, username=user.username, password=password)
		except:
			messages.error(request, 'User with this email does not exists')
			return redirect('loginStudent')
                                    
		if user is not None and user.is_student==True:
			login(request, user)
			return redirect('HomeStudent')
		else:
			messages.error(request, 'Email OR password is incorrect')


	context = {}
	return render(request, 'student/login.html', context)




def logoutUser(request):
	logout(request)
	return redirect('loginStudent')    

@student_required
def StudentAccount(request):
	profile = request.user.student

	context = {'profile':profile}
	return render(request, 'student/account.html', context)

@student_required
def updateProfile(request):
	user = request.user
	profile = user.student
	form = ProfileForm(instance=profile)
	if request.method == 'POST':
		user_form = UserForm(request.POST, instance=user)
		if user_form.is_valid():
			user_form.save()

		form = ProfileForm(request.POST, request.FILES, instance=profile)
		if form.is_valid():
			form.save()
			return redirect('StudentAccount')


	context = {'form':form}
	return render(request, 'student/profile_form.html', context)