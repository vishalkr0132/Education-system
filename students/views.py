from django.shortcuts import render
from django.shortcuts import redirect,render,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from Home.models import students_sign_up
# from .models import Profiles
from django.contrib import messages
from django.http import FileResponse
from django.core.files.storage import default_storage
from django.http import Http404


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
    elif request.method == 'POST':
        Profile_Pic = request.FILES.get('Profile_Pic')
        First_Name = request.POST.get('First_Name')
        Last_Name = request.POST.get('Last_Name')
        Email = request.POST.get('Email') 
        Location = request.POST.get('Location')
        Phone = request.POST.get('Phone')
        Gender = request.POST.get('Gender')
        DOB = request.POST.get('DOB')
        About = request.POST.get('About')
        
        student = students_sign_up.objects.get(Email=request.user.email)

        # Check if a profile already exists for the student
        existing_profile = students_sign_up.objects.filter(Email=request.user.email).first()
        if existing_profile:
            # If a profile already exists, update the existing profile
            existing_profile.Profile_Pic = Profile_Pic
            existing_profile.First_Name = First_Name
            existing_profile.Last_Name = Last_Name
            existing_profile.Email = Email
            existing_profile.Location = Location
            existing_profile.Phone = Phone
            existing_profile.Gender = Gender
            existing_profile.DOB = DOB
            existing_profile.About = About
            existing_profile.save()
        else:
            # If no profile exists, create a new profile
            profile_data = students_sign_up(Student=student, Profile_Pic=Profile_Pic, First_Name=First_Name, Last_Name=Last_Name,
                                   Email=Email, Location=Location, Phone=Phone, Gender=Gender, DOB=DOB, About=About)
            profile_data.save()
        return redirect('student_profile')
    else:
        username = request.user.username
        try:
            profile = students_sign_up.objects.get(Email=username)
            profile = students_sign_up.objects.filter(Email=username)
        except students_sign_up.DoesNotExist:
            profile = None

        # Pass profile as a list to ensure it's iterable in the template
        context = {'profile': profile,}
        return render(request, 'student-profile.html',context)

def logout_view(request):
    logout(request)
    return redirect('/')