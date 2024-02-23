from django.shortcuts import render
from django.shortcuts import redirect,render,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from Home.models import students_sign_up
from .models import Profiles
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
        Email = request.POST.get('Email')  # Ensure 'Email' field is present in your HTML form
        Location = request.POST.get('Location')
        Phone = request.POST.get('Phone')
        Gender = request.POST.get('Gender')
        DOB = request.POST.get('DOB')
        about = request.POST.get('about')
        
        student = students_sign_up.objects.get(Email=request.user.email)  # Assuming email is unique

        # Check if a profile already exists for the student
        existing_profile = Profiles.objects.filter(Student=student).first()
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
            existing_profile.about = about
            existing_profile.save()
        else:
            # If no profile exists, create a new profile
            profile_data = Profiles(Student=student, Profile_Pic=Profile_Pic, First_Name=First_Name, Last_Name=Last_Name,
                                   Email=Email, Location=Location, Phone=Phone, Gender=Gender, DOB=DOB, about=about)
            profile_data.save()

        return redirect('student_profile')
    else:
        username = request.user.username
        try:
            student = students_sign_up.objects.get(Email=username)
            profile = Profiles.objects.filter(Student=student).first()
        except students_sign_up.DoesNotExist:
            profile = None

        # Pass profile as a list to ensure it's iterable in the template
        context = {'profile': [profile]} if profile else {'profile': []}
        return render(request, 'student-profile.html')


def logout_view(request):
    logout(request)
    return redirect('/')