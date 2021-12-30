from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.views.generic import *
from school.forms import *
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages

from school.forms import *
from school.decorators import *
from student.filters import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


class SchoolSignUpView(CreateView):
    model = User
    form_class = SchoolSignUp
    template_name = 'school/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'School'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('loginSchool')


def LoginSchool(request):
    
	if request.user.is_authenticated and request.user.is_school==True:
		return redirect('HomeSchool')
	if request.method == 'POST':
		email = request.POST.get('email')
		password =request.POST.get('password')
		try:
			user = User.objects.get(email=email)
			user = authenticate(request, username=user.username, password=password)
		except:
			messages.error(request, 'User with this email does not exists')
			return redirect('loginSchool')
                                    
		if user is not None and user.is_school==True:
			login(request, user)
			return redirect('HomeSchool')
		else:
			messages.error(request, 'Email OR password is incorrect')


	context = {}
	return render(request, 'school/loginschool.html', context)


# def createPost(request):
# 	form = PostForm()

# 	if request.method == 'POST':
# 		form = PostForm(request.POST, request.FILES)
# 		if form.is_valid():
# 			form.save()
# 		return redirect('posts')

# 	context = {'form':form}
# 	return render(request, 'School/post_School.html', context)


#CRUD POST
@school_required 
def createPost(request):
    form = PostForm()
    if request.method =='POST':
        form = PostForm(request.POST , request.FILES )  
        if form.is_valid():
              
            obj = form.save(commit = False)
            obj.school = request.user.school;
            obj.save()
            form = PostForm()
            messages.success(request, "Successfully created")
            return redirect('PostsSchool')
          
  
    return render(request, 'school/post_school.html', {'form':form})  


@school_required
def updatePost(request, slug):
	post = PostSchool.objects.get(slug=slug, school  = request.user.school)
	form = PostForm(instance=post)

	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			form.save()
		return redirect('PostsSchool')

	context = {'form':form}
	return render(request, 'school/post_school.html', context)

@school_required
def deletePost(request, slug):
	post = PostSchool.objects.get(slug=slug, school = request.user.school)

	if request.method == 'POST':
		post.delete()
		return redirect('PostsSchool')
	context = {'item':post}
	return render(request, 'school/delete.html', context)




def logoutUser(request):
	logout(request)
	return redirect('HomeSchool')    




  

@school_required
def SchoolAccount(request):
	profile = request.user.school

	context = {'profile':profile}
	return render(request, 'school/accountSchool.html', context)

@school_required
def updateProfileSchool(request):
	user = request.user
	profile = user.school
	form = ProfileFormSchool(instance=profile)
	if request.method == 'POST':
		user_form = UserForm(request.POST, instance=user)
		if user_form.is_valid():
			user_form.save()

		form = ProfileFormSchool(request.POST, request.FILES, instance=profile)
		if form.is_valid():
			form.save()
			return redirect('SchoolAccount')


	context = {'form':form}
	return render(request, 'school/school_form.html', context)




# @school_required
# def post(request, slug):
# 	post = PostSchool.objects.get(slug=slug, School = request.user.School)
#     group = PostSchool.objects.get(slug=slug, School = request.user.School)
# 	context = {'post':post}
# 	return render(request, 'School/postSchool.html', context)
@school_required
def post(request, slug):
      post = PostSchool.objects.get(slug=slug, school = request.user.school)
      groups = GroupeSchool.objects.filter(postschool = post)
      context = {'post':post, 'groups':groups}
      return render(request, 'School/postSchool.html', context)
      
      

@school_required
def creategroup(request,slug):
    form = GroupsForm()
    if request.method =='POST':
        form = GroupsForm(request.POST , request.FILES )  
        if form.is_valid():
              
            obj = form.save(commit = False)
            obj.postschool = PostSchool.objects.get(slug=slug, school = request.user.school)
            obj.save()
            form = GroupsForm()
            messages.success(request, "Successfully created")
            return redirect('PostsSchool')
          
  
    return render(request, 'School/groups.html', {'form':form})    



@school_required
def postsSchool(request):
	posts = PostSchool.objects.filter(school = request.user.school)
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
	return render(request, 'School/PostsSchool.html', context)



@school_required
def homeSchool(request):
    return render(request, 'school/HomeSchool.html')