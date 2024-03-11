from django.shortcuts import render
from django.shortcuts import redirect,render,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from Home.models import students_sign_up
from.models import *
from django.contrib import messages
from django.http import FileResponse
from django.http import Http404
import os
from .forms import *

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
        if 'profile_submit' in request.POST:
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
        
        elif 'resume_submit' in request.POST:
            resume_file = request.FILES.get('Resume')
            if resume_file:
                student_profile_instance = students_sign_up.objects.filter(Email=request.user.email).first()
                if student_profile_instance:
                    existing_resume = Resumes.objects.filter(user=request.user).first()
                    if existing_resume:
                        existing_resume.resume = resume_file
                        existing_resume.save()
                        messages.success(request, 'Resume updated successfully!')
                    else:
                        resume = Resumes.objects.create(user=request.user, resume=resume_file)
                        resume.save()
                        messages.success(request, 'Resume uploaded successfully!')
                else:
                    messages.error(request, 'Student profile not found.')
            else:
                messages.error(request, 'No resume file selected.')
            return redirect('student_profile')
        
        elif 'resume_headline_submit' in request.POST:
            form = Resume_headlineForm(request.POST)
            if form.is_valid():
                existing_resume_headline = ResumeHeadline.objects.filter(user=request.user).first()
                if existing_resume_headline:
                    existing_resume_headline.Resume_headline_data = form.cleaned_data['Resume_headline_data']
                    existing_resume_headline.save()
                    messages.success(request, 'Resume headline updated successfully!')
                else:
                    resume_headline = form.save(commit=False)
                    resume_headline.user = request.user
                    resume_headline.save()
                    messages.success(request, 'Resume headline created successfully!')
                    return redirect('student_profile')  # Replace 'student_profile' with your actual profile page URL
        elif 'Education_Submit' in request.POST:
            education_instance = Educationdata.objects.filter(user=request.user).first()
            education_data = EducationdataForm(request.POST, instance=education_instance)
            if education_data.is_valid():
                education_instance = education_data.save(commit=False)
                education_instance.user = request.user  # Set the user field
                education_instance.save()
                messages.success(request, 'Education data updated successfully!')
            else:
                print(education_data.errors)  # Print out form errors
                messages.error(request, 'Error updating education data. Please check the form data.')
            return redirect('student_profile')  # Redirect to the student profile page
        
        elif 'Inter_submit' in request.POST:
            intern_instance = Internshipdetails.objects.filter(user=request.user).first()
            Intern_data = InternshipDetailsForm(request.POST, instance=intern_instance)
            if Intern_data.is_valid():
                intern_instance = Intern_data.save(commit=False)
                intern_instance.user = request.user  # Set the user field
                intern_instance.save()
                messages.success(request, 'Internship data updated successfully!')
            else:
                print(Intern_data.errors)  # Print out form errors
                messages.error(request, 'Error updating internship data. Please check the form data.')
            return redirect('student_profile')  # Redirect to the student profile page
        
        elif 'Project_submit' in request.POST:
            project_instance = Projectdetails.objects.filter(user=request.user).first()
            Project_data = ProjectDetailsForm(request.POST, instance=project_instance)
            if Project_data.is_valid():
                project_instance = Project_data.save(commit=False)
                project_instance.user = request.user  # Set the user field
                project_instance.save()
                messages.success(request, 'Project data updated successfully!')
            else:
                print(Project_data.errors)  # Print out form errors
                messages.error(request, 'Error updating Project data. Please check the form data.')
            return redirect('student_profile')  # Redirect to the student profile page
        
        elif 'Certifiace_submit' in request.POST:
            Certiface_instance = Certificatedetails.objects.filter(user=request.user).first()
            Certiface_data = CertificateDetailsForm(request.POST, instance=Certiface_instance)
            if Certiface_data.is_valid():
                Certiface_instance = Certiface_data.save(commit=False)
                Certiface_instance.user = request.user  # Set the user field
                Certiface_instance.save()
                messages.success(request, 'Certifiace data updated successfully!')
            else:
                print(Certiface_data.errors)  # Print out form errors
                messages.error(request, 'Error updating Certifiace data. Please check the form data.')
            return redirect('student_profile')  # Redirect to the student profile page
        
        elif 'Competative_Exam' in request.POST:
            Competitive_instance = Competitivedetails.objects.filter(user=request.user).first()
            Competitive_data = CompetitivedetailsForm(request.POST, instance=Competitive_instance)
            if Competitive_data.is_valid():
                Competitive_instance = Competitive_data.save(commit=False)
                Competitive_instance.user = request.user  # Set the user field
                Competitive_instance.save()
                messages.success(request, 'Competative data updated successfully!')
            else:
                print(Competitive_data.errors)  # Print out form errors
                messages.error(request, 'Error updating Competative data. Please check the form data.')
            return redirect('student_profile')  # Redirect to the student profile page
        
        elif 'Work_Submit' in request.POST:
            Work_instance = EmploymentDetails.objects.filter(user=request.user).first()
            Work_data = EmploymentDetailsForm(request.POST, instance=Work_instance)
            if Work_data.is_valid():
                Work_instance = Work_data.save(commit=False)
                Work_instance.user = request.user  # Set the user field
                Work_instance.save()
                messages.success(request, 'Work data updated successfully!')
            else:
                print(Work_data.errors)  # Print out form errors
                messages.error(request, 'Error updating Work data. Please check the form data.')
            return redirect('student_profile')  # Redirect to the student profile page
        
        elif 'Award_submit' in request.POST:
            Award_instance = AwardDetails.objects.filter(user=request.user).first()
            Award_data = AwardDetailsForm(request.POST, instance=Award_instance)
            if Award_data.is_valid():
                Award_instance = Award_data.save(commit=False)
                Award_instance.user = request.user
                Award_instance.save()
                messages.success(request, 'Work data updated successfully!')
                return redirect('student_profile')
            else:
                print(Award_data.errors)
                messages.error(request, 'Error updating Work data. Please check the form data.')
            return redirect('student_profile')
        
        elif 'Acadmic_Achive' in request.POST:
            Acadmic_instance = AcadmicDetails.objects.filter(user=request.user).first()
            Acadmic_data = AcadmicDetailsForm(request.POST, instance=Acadmic_instance)
            if Acadmic_data.is_valid():
                Acadmic_instance = Acadmic_data.save(commit=False)
                Acadmic_instance.user = request.user
                Acadmic_instance.save()
                messages.success(request, 'Acadmic data updated successfully!')
                return redirect('student_profile')
            else:
                print(Acadmic_data.errors)
                messages.error(request, 'Error Acadmic Work data. Please check the form data.')
            return redirect('student_profile')

        if 'Language_Submit' in request.POST:
            communication_instance = Communication.objects.filter(user=request.user).first()
            communication_data = CommunicationForm(request.POST, instance=communication_instance)
            if communication_data.is_valid():
                communication_instance = communication_data.save(commit=False)
                communication_instance.user = request.user
                communication_instance.save()
                messages.success(request, 'Communication language data updated successfully!')
            else:
                print(communication_data.errors)
                messages.error(request, 'Error updating communication language data. Please check the form data.')
            return redirect('student_profile')
    
    else:
        Acadmic_data = AcadmicDetails.objects.filter(user=request.user).first()
        Award_data = AwardDetails.objects.filter(user=request.user).first()
        Competative_data = Competitivedetails.objects.filter(user=request.user).first()
        Certificate_data = Certificatedetails.objects.filter(user=request.user).first()
        Project_data = Projectdetails.objects.filter(user=request.user).first()
        Intern_data = Internshipdetails.objects.filter(user=request.user).first()
        Communication_data = Communication.objects.filter(user=request.user).first()
        Education_data_form = Educationdata.objects.filter(user=request.user).first()
        resume = Resumes.objects.filter(user=request.user).first()
        Resume_headline = ResumeHeadline.objects.filter(user=request.user).first()
        username = request.user.username
        try:
            # profile = students_sign_up.objects.filter(Email=username)
            profile = students_sign_up.objects.filter(user=request.user)
            profile_photo = students_sign_up.objects.filter(Email=username).first().Profile_Pic
            if profile_photo =="":
                profile_photo = "01.jpg"
        except students_sign_up.DoesNotExist:
            profile = None
        context = {
            'profile': profile,
            'resume': resume,
            'Resume_headline': Resume_headline,
            'Education_data_form': Education_data_form,
            'Communication_data': Communication_data,
            'Intern_data': Intern_data,
            'Project_data': Project_data,
            'Certificate_data': Certificate_data,
            'Competative_data': Competative_data,
            'Award_data': Award_data,
            'Acadmic_data': Acadmic_data,
         } 
        return render(request, 'student-profile.html', context)
    
def logout_view(request):
    logout(request)
    return redirect('/')

def forgot_password(request):
    return redirect(request ,'forgot-password.html')