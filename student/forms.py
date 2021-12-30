from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import transaction
from student.models import *
from Home.models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, matier):
        return '%s' % matier.Matier

class UserSignUp(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone = forms.IntegerField(required=True)
    wilaya = forms.ModelChoiceField(
        queryset=Wilaya.objects.all(),
        widget=forms.RadioSelect,
        required=True,
    )
    level = forms.ModelChoiceField(
        queryset=Level.objects.all(),
        widget=forms.RadioSelect,
        required=True
    )
    division = forms.ModelChoiceField(
        queryset=Division.objects.all(),
        widget=forms.RadioSelect,
        required=True
    )
    annee = forms.ModelChoiceField(
        queryset=Annee.objects.all(),
        widget=forms.RadioSelect,
        required=True
    )
    matier = CustomMMCF(
        queryset=Matier.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    
    
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email','first_name','last_name','phone','wilaya','level','division','annee','matier','password1', 'password2']
        
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.is_active = True
        user.username = self.cleaned_data.get('email')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        phone = self.cleaned_data.get('phone')
        wilaya = self.cleaned_data.get('wilaya')
        level = self.cleaned_data.get('level')
        division = self.cleaned_data.get('division')
        annee = self.cleaned_data.get('annee')
        student = Student.objects.create(user=user,first_name=user.first_name, last_name = user.last_name,email=user.email,phone=phone,wilaya=wilaya
                                         ,level=level,division=division,annee=annee
                                         )
        student.matier.add(*self.cleaned_data.get('matier'))
       
        student.save()
        return user
    

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"    
        exclude = ['user']
        

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')