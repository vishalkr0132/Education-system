from django.shortcuts import render
from django.shortcuts import redirect,render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import students_sign_up,colleges_sign_up,instructors_sign_up,partner_sign_up
from django.contrib.auth.models import Group
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils import timezone
from .send_email import email_sending
import random

# Create your views here.
def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('Email')
        password = request.POST.get('Password')
        
        user = authenticate(username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            messages.error(request, 'You do not belong to any user.')
            return redirect('/admins/') 
        else:
            messages.error(request, 'Username and Password are incorrect.')
            return redirect('/') 
    else:
        return render(request, 'sign-in.html')

def student_sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('Email')
        password = request.POST.get('Password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.error(request, 'You do not belong to any user.')
            return redirect('./students/')
        else:
            messages.error(request, 'Username and Password are incorrect.')
            return redirect('/student_sign_in')
    else:
        return render(request,'student-sign-in.html')

def college_sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('Email')
        password = request.POST.get('Password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.error(request, 'You do not belong to any user.')
            return redirect('./colleges/')
        else:
            messages.error(request, 'Username and Password are incorrect.')
            return redirect('/college_sign_in')
    else:
        return render(request,'college-sign-in.html')

def instructor_sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('Email')
        password = request.POST.get('Password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.error(request, 'You do not belong to any user.')
            return redirect('./instructor/')
        else:
            messages.error(request, 'Username and Password are incorrect.')
            return redirect('/instructor_sign_in')
    else:
        return render(request,'instructor-sign-in.html')

def partners_sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('Email')
        password = request.POST.get('Password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.error(request, 'You do not belong to any user.')
            return redirect('./partners/')
        else:
            messages.error(request, 'Username and Password are incorrect.')
            return redirect('/partners_sign_in')
    else:
        return render(request,'partners-sign-in.html')

def sign_up(request):
    return render(request,'sign-up.html')

# def student_sign_up(request):
#     if request.method == 'POST':
#         First_Name = request.POST.get('First_Name')
#         Last_Name = request.POST.get('Last_Name')
#         Email = request.POST.get('Email')
#         Password = request.POST.get('Password')
        
#         Student_Register = students_sign_up(First_Name = First_Name, Last_Name = Last_Name, Email = Email, Password = Password)
        
#          # Check if email already exists
#         if User.objects.filter(email=Email).exists():
#             messages.error(request, 'Email is already taken. Please choose a different one.')
#             return redirect('/student_sign_up')
#         Student_Register.save()
#         user = User.objects.create_user(Email,Email,Password)
#         user.save()
#         messages.success(request, 'Registration successful. You can now log in.')
#         return redirect('/student_sign_in')
#     else:
#         return render(request,'student-sign-up.html')

def student_sign_up(request):
    if request.method == 'POST':
        First_Name = request.POST.get('First_Name')
        Last_Name = request.POST.get('Last_Name')
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        
        # Check if email already exists
        if User.objects.filter(email=Email).exists():
            messages.error(request, 'Email is already taken. Please choose a different one.')
            return redirect('/student_sign_up')
        
        # Create a new User instance
        user = User.objects.create_user(username=Email, email=Email, password=Password)
        
        # Create a new students_sign_up instance and associate it with the created user
        Student_Register = students_sign_up.objects.create(
            user=user,
            First_Name=First_Name,
            Last_Name=Last_Name,
            Email=Email,
            Password=Password,
            created_at=timezone.now(),
            Date=timezone.now(),  # This should be set to a meaningful value
            Location='',          # You can adjust this based on your requirements
            Phone='',             # You can adjust this based on your requirements
            Gender='',            # You can adjust this based on your requirements
            DOB=None,             # You can adjust this based on your requirements
            About='',             # You can adjust this based on your requirements
            Profile_Pic=''        # You can adjust this based on your requirements
        )
        
        messages.success(request, 'Registration successful. You can now log in.')
        return redirect('/student_sign_in')
    else:
        return render(request, 'student-sign-up.html')

def college_sign_up(request):
    if request.method == 'POST':
        College_Name = request.POST.get('College_Name')
        College_Code = request.POST.get('College_Code')
        Admin_Administrator = request.POST.get('Admin_Administrator')
        Phone = request.POST.get('Phone')
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        
        College_Register = colleges_sign_up(College_Name = College_Name, College_Code = College_Code,Admin_Administrator = Admin_Administrator, Phone = Phone, Email = Email, Password = Password)
        
        # Check if email already exists
        if User.objects.filter(email=Email).exists():
            messages.error(request, 'Email is already taken. Please choose a different one.')
            return redirect('/college_sign_up')
        College_Register.save()
        
        user = User.objects.create_user(Email,Email,Password)
        user.save()
        messages.success(request, 'Registration successful. You can now log in.')
        return redirect('/college_sign_in')
    else:
        return render(request,'college-sign-up.html')

def instructor_sign_up(request):
    if request.method == 'POST':
        Full_Name = request.POST.get('Full_Name')
        Phone = request.POST.get('Phone')
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        
        Instructor_Register = instructors_sign_up(Full_Name = Full_Name, Phone = Phone, Email = Email, Password = Password)
        
        # Check if email already exists
        if User.objects.filter(email=Email).exists():
            messages.error(request, 'Email is already taken. Please choose a different one.')
            return redirect('/instructor_sign_up')
        Instructor_Register.save()
        
        user = User.objects.create_user(Email,Email,Password)
        user.is_active = False
        user.save()
        messages.success(request, 'Registration successful. You can now log in.')
        return redirect('/instructor_sign_in')
    else:
        return render(request,'instructor-sign-up.html')

def partners_sign_up(request):
    if request.method == 'POST':
        Organigation_Name = request.POST.get('Organigation_Name')
        Admin_Administrator = request.POST.get('Admin_Administrator')
        Phone = request.POST.get('Phone')
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        
        Partner_Register = partner_sign_up(Organigation_Name = Organigation_Name, Admin_Administrator = Admin_Administrator, Phone = Phone, Email = Email, Password = Password)
        
        # Check if email already exists
        if User.objects.filter(email=Email).exists():
            messages.error(request, 'Email is already taken. Please choose a different one.')
            return redirect('/instructor_sign_up')
        Partner_Register.save()
        
        user = User.objects.create_user(Email,Email,Password)
        user.save()
        messages.success(request, 'Registration successful. You can now log in.')
        return redirect('/instructor_sign_in')
    else:
        return render(request,'partners-sign-up.html')

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        msg = random.randint(000000, 999999 )
        email_sending(email, str(msg))     
        return render(request, 'change_password.html', {'msg':msg, 'email':email} )   
    return render(request,'forgot-password.html')

def change_password(request):
    if request.method == 'POST':
        otp_val = request.POST.get('otp_ver')
        otp = request.POST.get('otp')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if otp == otp_val:
            user = User.objects.get(email=email)
            user.set_password(password)
            user.save()
            return redirect('/student_sign_in')
        else:
            return HttpResponse("OTP DIdnt Match")
    else:
        return redirect('/student_sign_in')
    