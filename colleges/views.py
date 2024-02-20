from django.shortcuts import render
from django.shortcuts import redirect,render,HttpResponse
from django.contrib.auth import logout
from admins.models import signup

# Create your views here.

def instructor_dashboard(request):
    if request.user.is_anonymous:
        return redirect('/')
    else:
        username = request.user.username
        instructor = signup.objects.filter(Email=username)
        context = {'instructor': instructor}
    return render(request,'instructor-dashboard.html',context)

def admin_instructor_detail(request):
    return render(request,'admin-instructor-detail.html')

def logout_view(request):
    logout(request)
    return redirect('/')