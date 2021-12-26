from django.shortcuts import render

# Create your views here.
def homeSchool(request):
    return render(request, 'school/HomeSchool.html')