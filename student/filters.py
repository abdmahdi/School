import django_filters
from django_filters import CharFilter
from school.models import PostSchool
from teacher.models import *


from django import forms

from .models import *

class PostFilter(django_filters.FilterSet):
	headline = CharFilter(field_name='title', lookup_expr="icontains", label='Title')
	matier = django_filters.ModelMultipleChoiceFilter(queryset=Matier.objects.all(),
		widget=forms.CheckboxSelectMultiple
		)
	class Meta:
		model = PostTeacher
		fields = ['matier','level','division','Annee']
  

class PostFilterSchool(django_filters.FilterSet):
	headline = CharFilter(field_name='title', lookup_expr="icontains", label='Title')
	matier = django_filters.ModelMultipleChoiceFilter(queryset=Matier.objects.all(),
		widget=forms.CheckboxSelectMultiple
		)
	class Meta:
		model = PostSchool
		fields = ['matier','level','division','Annee']  