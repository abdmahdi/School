
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import transaction
from teacher.models import *
from Home.models import *
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm



class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, matier):
        return '%s' % matier.Matier

class TeacherSignUp(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone = forms.IntegerField(required=True)
    wilaya = forms.ModelChoiceField(
        queryset=Wilaya.objects.all(),
        widget=forms.RadioSelect,
        required=True,
    )
    adress = forms.CharField(required=True)
    bio = forms.Textarea()
    
    level = forms.ModelChoiceField(
        queryset=Level.objects.all(),
        widget=forms.RadioSelect,
        required=True
    )
    matier = CustomMMCF(
        queryset=Matier.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    
    
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email','first_name','last_name','phone','adress','wilaya','level','matier','bio','password1', 'password2']
        
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.is_active = True
        user.username = self.cleaned_data.get('email')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        phone = self.cleaned_data.get('phone')
        wilaya = self.cleaned_data.get('wilaya')
        level = self.cleaned_data.get('level')
        adress = self.cleaned_data.get('adress')
        bio = self.cleaned_data.get('bio')
        
        
        # pic = self.cleaned_data.get('pic')
        teacher = Teacher.objects.create(user=user,first_name=user.first_name, last_name = user.last_name,email=user.email,phone=phone,wilaya=wilaya
                                         ,level=level,adress=adress,bio=bio
                                         )
        teacher.matier.add(*self.cleaned_data.get('matier'))
       
        teacher.save()
        return user
    
class GroupsForm(forms.ModelForm):
    starttime =  forms.TimeField(label='Start Time', label_suffix=" : ",
                             required=True, disabled=False, input_formats=["%H:%M"],
                             widget=forms.TimeInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})
    endstime = forms.TimeField(label='Ends Time', label_suffix=" : ",
                             required=True, disabled=False, input_formats=["%H:%M"],
                             widget=forms.TimeInput(attrs={'class': 'form-control'}),
                             error_messages={'required': "This field is required."})
    class Meta:
        model = Groupe
        fields = ("N_groupe","Days","starttime","endstime","nombredeplace")


class PostForm(forms.ModelForm):
    
	class Meta:
		model = PostTeacher
		fields = '__all__'
		exclude = ['teacher','slug']
        

        
class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email']


class ProfileFormTeacher(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"    
        exclude = ['user']






  
  
 
		
    
    
    
         
    	
    