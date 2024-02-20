from django.shortcuts import render
from django.shortcuts import redirect,render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages
from admins.models import signup
from django.contrib.auth.models import Group

# Create your views here.

# def sign_up(request):
#     if request.method == 'POST':
#         User_Type = request.POST.get('User_Type')
#         First_Name = request.POST.get('First_Name')
#         Last_Name = request.POST.get('Last_Name')
#         Mobile = request.POST.get('Mobile')
#         Email = request.POST.get('Email')
#         Password = request.POST.get('Password')
#         Confirm_Password = request.POST.get('Confirm_Password')
        
#         Resister = signup(User_Type = User_Type, First_Name = First_Name, Last_Name=Last_Name,Mobile=Mobile,Email=Email,Password=Password,Confirm_Password=Confirm_Password)
        
#         # Check if email already exists
#         if User.objects.filter(email=Email).exists():
#             messages.error(request, 'Email is already taken. Please choose a different one.')
#             return redirect('/sign_up')
#         Resister.save()
        
#         # Create the user with email as username
#         user = User.objects.create_user(username=Email, email=Email, password=Password)
#         user.first_name = First_Name
#         user.last_name = Last_Name
#         user.mobile = Mobile
#         user.save()
        
#         # Assign user to group based on User_Type
#         group_name = User_Type.capitalize()
#         group, created = Group.objects.get_or_create(name=group_name)
#         user.groups.add(group)
        
#         messages.success(request, 'Registration successful. You can now log in.')
#         return redirect('/')
#     else:
#         return render(request, 'sign-up.html')
    
# # Start login form
# def loginuser(request):
#     if request.method == "POST":
#         email = request.POST.get('Email')
#         password = request.POST.get('Password')
        
#         user = authenticate(username=email, password=password)
#         if user is not None:
#             login(request, user)
            
#             # Check user's group and redirect accordingly
#             if user.groups.filter(name='Admin').exists():
#                 return redirect('admin_dashboard')
#             elif user.groups.filter(name='Collage').exists():
#                 return redirect('collage/collage_dashboard')
#             elif user.groups.filter(name='Student').exists():
#                 return redirect('students/student_dashboard')
#             elif user.groups.filter(name='Company').exists():
#                 return redirect('companys/company_dashboard')
#             elif user.groups.filter(name='Instructor').exists():
#                 return redirect('instructor/instructor_dashboard')
#             elif user.groups.filter(name='Partner').exists():
#                 return redirect('partner/partner_dashboard')
#             else:
#                 # Handle case where user is not assigned to any group
#                 messages.error(request, 'You do not belong to any user.')
#                 return redirect('/')
#         else:
#             messages.error(request, 'Username and Password are incorrect.')
#             return redirect('/')
#     else:
#          return render(request,'sign-in.html')
     
def logout_view(request):
    logout(request)
    return redirect('/')

def forgot_password(request):
    return render(request,'forgot-password.html')

def admin_dashboard(request):
    if request.user.is_anonymous:
        return redirect('/')
    else:
        username = request.user.username
        Admin = signup.objects.filter(Email=username)
        context = {'Admin': Admin}
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
        return render(request,'admin-student-list.html')
    
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

