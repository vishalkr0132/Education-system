from django.shortcuts import render
from django.shortcuts import redirect,render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages
from admins.models import signup
from django.contrib.auth.models import Group

# Create your views here.

def loginuser(request):
    return render(request,'sign-in.html')

def student_sign_in(request):
    return render(request,'student-sign-in.html')

def college_sign_in(request):
    return render(request,'college-sign-in.html')

def instructor_sign_in(request):
    return render(request,'instructor-sign-in.html')

def partners_sign_in(request):
    return render(request,'partners-sign-in.html')

def Company_sign_in(request):
    return render(request,'company-sign-in.html')

def sign_up(request):
    return render(request,'sign-up.html')

def student_sign_up(request):
    return render(request,'student-sign-up.html')

def college_sign_up(request):
    return render(request,'college-sign-up.html')

def instructor_sign_up(request):
    return render(request,'instructor-sign_up.html')

def partners_sign_up(request):
    return render(request,'partners-sign-up.html')

def Company_sign_up(request):
    return render(request,'company-sign-up.html')

def forgot_password(request):
    return render(request,'forgot-password.html')
