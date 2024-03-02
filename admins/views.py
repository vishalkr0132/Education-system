from django.shortcuts import render
from django.shortcuts import redirect,render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages
from admins.models import signup
from Home.models import students_sign_up
from django.contrib.auth.models import Group
from students.models import *

# Create your views here.
     
def logout_view(request):
    logout(request)
    return redirect('/')

def forgot_password(request):
    return render(request,'forgot-password.html')

def admin_profile(request):
    return render(request,'admin-profile.html')

def admin_dashboard(request):
    if request.user.is_anonymous:
        return redirect('/')
    elif request.user.is_superuser:
        superuser = User.objects.get(username=request.user.username)
        first_name = superuser.first_name
        last_name = superuser.last_name
        context = {'first_name': first_name, 'last_name': last_name}
        return render(request, 'admin-dashboard.html', context)
    else:
        username = request.user.username
        admin_user = signup.objects.filter(Email=username).first()
        context = {'Admin': admin_user}
        return render(request, 'admin-dashboard.html', context)

def admin_instructor_detail(request):
    if request.user.is_anonymous:
        return redirect('/')
    else:
        return render(request,'admin-instructor-detail.html')

def admin_instructor_list(request):
    if request.user.is_anonymous:
        return redirect('/')
    else:
        return render(request,'admin-instructor-list.html')

def admin_instructor_request(request):
    if request.user.is_anonymous:
        return redirect('/')
    else:
        return render(request,'admin-instructor-request.html')

def admin_student_list(request):
    if request.user.is_anonymous:
        return redirect('/')
    else:
        Student = students_sign_up.objects.all()
        data={'Student':Student}
        return render(request,'admin-student-list.html',data)
    
def admin_student_detail(request, Pid):
    if request.user.is_anonymous:
        return redirect('/')
    else:
        # email = students_sign_up.objects.get(id=Pid)
        # email = email.Email
        detail = students_sign_up.objects.filter(id=Pid)
        username = students_sign_up.objects.get(id=Pid)
        username = username.user
        education_data  = Educationdata.objects.get(user=username)
        data = {'detail': detail, 'education_data':education_data }
        return render(request, 'admin-student-detail.html', data)
    
def admin_course_list(request):
    if request.user.is_anonymous:
        return redirect('/')
    else:
        return render(request,'admin-course-list.html')

def admin_course_category(request):
    if request.user.is_anonymous:
        return redirect('/')
    else:
        return render(request,'admin-course-category.html')
    
def admin_course_detail(request):
    if request.user.is_anonymous:
        return redirect('/')
    else:
        return render(request,'admin-course-detail.html')

def instructor_create_course(request):
    if request.user.is_anonymous:
        return redirect('/')
    else:
        return render(request,'instructor-create-course.html')

def admin_edit_course_detail(request):
    if request.user.is_anonymous:
        return redirect('/')
    else:
        return render(request,'admin-edit-course-detail.html')

def admin_college_list(request):
    if request.user.is_anonymous:
        return redirect('/')
    else:
        return render(request,'admin-college-list.html')
