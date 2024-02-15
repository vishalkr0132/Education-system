from django.shortcuts import render
from django.shortcuts import redirect,render,HttpResponse
from django.contrib.auth import logout
from admins.models import signup

# Create your views here.

# def student_dashboard(request):
#     if request.user.is_anonymous:
#         return redirect('/')
#     else:
#         username = request.user.username
#         Admin = signup.objects.filter(Email=username)
#         Admin = signup.objects.all()
#         Admin_Name = {'Admin': Admin, 'Admin': Admin}
#         return render(request, 'admin-dashboard.html', Admin_Name)

def student_dashboard(request):
    if request.user.is_anonymous:
        return redirect('/')
    else:
        username = request.user.username
        Student = signup.objects.filter(Email=username)
        context = {'Student': Student}
        return render(request, 'student-dashboard.html', context)

def admin_student_list(request):
    return render(request,'admin-student-list.html')

def logout_view(request):
    logout(request)
    return redirect('/')