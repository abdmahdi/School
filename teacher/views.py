from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib.auth import login
from django.views.generic import *
from teacher.forms import *
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from teacher.forms import *
from teacher.decorators import *
from student.filters import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUp
    template_name = 'teacher/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('loginTeacher')


def LoginTeacher(request):
    
	if request.user.is_authenticated and request.user.is_teacher==True:
		return redirect('HomeTeacher')
	if request.method == 'POST':
		email = request.POST.get('email')
		password =request.POST.get('password')
		try:
			user = User.objects.get(email=email)
			user = authenticate(request, username=user.username, password=password)
		except:
			messages.error(request, 'User with this email does not exists')
			return redirect('loginTeacher')
                                    
		if user is not None and user.is_teacher==True:
			login(request, user)
			return redirect('HomeTeacher')
		else:
			messages.error(request, 'Email OR password is incorrect')


	context = {}
	return render(request, 'teacher/login.html', context)


# def createPost(request):
# 	form = PostForm()

# 	if request.method == 'POST':
# 		form = PostForm(request.POST, request.FILES)
# 		if form.is_valid():
# 			form.save()
# 		return redirect('posts')

# 	context = {'form':form}
# 	return render(request, 'teacher/post_teacher.html', context)


#CRUD POST
@teacher_required 
def createPost(request):
    form = PostForm()
    if request.method =='POST':
        form = PostForm(request.POST , request.FILES )  
        if form.is_valid():
              
            obj = form.save(commit = False)
            obj.teacher = request.user.teacher;
            obj.save()
            form = PostForm()
            messages.success(request, "Successfully created")
            return redirect('HomeTeacher')
          
  
    return render(request, 'teacher/post_teacher.html', {'form':form})  


@teacher_required
def updatePost(request, slug):
	post = PostTeacher.objects.get(slug=slug, teacher  = request.user.teacher)
	form = PostForm(instance=post)

	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			form.save()
		return redirect('HomeTeacher')

	context = {'form':form}
	return render(request, 'teacher/post_teacher.html', context)

@teacher_required
def deletePost(request, slug):
	post = PostTeacher.objects.get(slug=slug, teacher = request.user.teacher)

	if request.method == 'POST':
		post.delete()
		return redirect('HomeTeacher')
	context = {'item':post}
	return render(request, 'teacher/delete.html', context)




def logoutUser(request):
	logout(request)
	return redirect('HomeSchool')    




  

@teacher_required
def TeacherAccount(request):
	profile = request.user.teacher

	context = {'profile':profile}
	return render(request, 'teacher/accountTeacher.html', context)

@teacher_required
def updateProfileTeacher(request):
	user = request.user
	profile = user.teacher
	form = ProfileFormTeacher(instance=profile)
	if request.method == 'POST':
		user_form = UserForm(request.POST, instance=user)
		if user_form.is_valid():
			user_form.save()

		form = ProfileFormTeacher(request.POST, request.FILES, instance=profile)
		if form.is_valid():
			form.save()
			return redirect('TeacherAccount')


	context = {'form':form}
	return render(request, 'teacher/teacher_form.html', context)




@teacher_required
def post(request, slug):
	post = PostTeacher.objects.get(slug=slug, teacher = request.user.teacher)
	context = {'post':post}
	return render(request, 'teacher/postteacher.html', context)
  

@teacher_required
def creategroup(request):
    form = GroupsForm()
    if request.method =='POST':
        form = GroupsForm(request.POST , request.FILES )  
        if form.is_valid():
              
            obj = form.save(commit = False)
            obj.save()
            form = GroupsForm()
            messages.success(request, "Successfully created")
            return redirect('createPost')
          
  
    return render(request, 'teacher/groups.html', {'form':form})    



@teacher_required
def poststeacher(request):
	posts = PostTeacher.objects.filter(teacher = request.user.teacher)
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
	return render(request, 'teacher/PostsTeacher.html', context)



@teacher_required
def hometeacher(request):
    return render(request, 'teacher/HomeTeacher.html')