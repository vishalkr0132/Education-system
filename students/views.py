from django.shortcuts import render
from django.shortcuts import redirect,render,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from Home.models import students_sign_up
from django.contrib import messages
from django.http import FileResponse
from django.http import Http404
import os

# Create your views here.
def admin_student_list(request):
    return render(request,'admin-student-list.html')

def student_dashboard(request):
    if request.user.is_anonymous:
        return redirect('/')
    else:
        username = request.user.username
        Student = students_sign_up.objects.filter(Email=username)
        context = {'Student': Student}
        return render(request, 'student-dashboard.html', context)

def student_profile(request):
    if request.user.is_anonymous:
        return redirect('/')

    if request.method == 'POST':
        existing_profile = students_sign_up.objects.filter(Email=request.user.email).first()
        if existing_profile:
            form_data = {
                'First_Name': request.POST.get('First_Name'),
                'Last_Name': request.POST.get('Last_Name'),
                'Location': request.POST.get('Location'),
                'Phone': request.POST.get('Phone'),
                'Gender': request.POST.get('Gender'),
                'DOB': request.POST.get('DOB'),
                'About': request.POST.get('About')
            }
            if 'Profile_Pic' in request.FILES:
                profile_pic = request.FILES['Profile_Pic']
                existing_profile.Profile_Pic = profile_pic
            existing_profile.__dict__.update(form_data)
            existing_profile.save()
        else:
            profile_data = students_sign_up.objects.create(
                Email=request.user.email,
                First_Name=request.POST.get('First_Name'),
                Last_Name=request.POST.get('Last_Name'),
                Location=request.POST.get('Location'),
                Phone=request.POST.get('Phone'),
                Gender=request.POST.get('Gender'),
                DOB=request.POST.get('DOB'),
                About=request.POST.get('About')
            )
            if 'Profile_Pic' in request.FILES:
                profile_data.Profile_Pic = request.FILES['Profile_Pic']
            profile_data.save()
            messages.success(request, 'Profile updated successfully!')
        return redirect('student_profile')

    else:
        username = request.user.username
        try:
            profile = students_sign_up.objects.get(Email=username)
            profile = students_sign_up.objects.filter(Email=username)
        except students_sign_up.DoesNotExist:
            profile = None

        context = {'profile': profile}
        return render(request, 'student-profile.html', context)
    
def logout_view(request):
    logout(request)
    return redirect('/')