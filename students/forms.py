from django import forms
from .models import *

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resumes
        fields = ['resume']
        
class Resume_headlineForm(forms.ModelForm):
    class Meta:
        model = ResumeHeadline
        fields = ['Resume_headline_data']
        

class EducationdataForm(forms.ModelForm):
    class Meta:
        model = Educationdata
        fields = ['College_Name', 'College_Start_Year', 'College_End_Year', 'Degree', 'Stream', 'Grading_System', 'Performance', 'Course_Type']
        
class CommunicationForm(forms.ModelForm):
    class Meta:
        model = Communication
        fields = ['Communication_Language']
        
class InternshipDetailsForm(forms.ModelForm):
    class Meta:
        model = Internshipdetails
        fields = ['Intern_Company_Name', 'Intern_Start_Month', 'Intern_Start_Year', 
                  'Intern_End_Month', 'Intern_End_Year', 'Intern_Project_Name', 
                  'Intern_Desc', 'Intern_Project_Url']

class ProjectDetailsForm(forms.ModelForm):
    class Meta:
        model = Projectdetails
        fields = ['Project_Name', 'Project_Start_Month', 'Project_Start_Year', 'Project_End_Month', 'Project_End_Year', 'Project_Desc', 'Project_Url']
        
class CertificateDetailsForm(forms.ModelForm):
    class Meta:
        model = Certificatedetails
        fields = ['Certificate_Name', 'Certificate_ID', 'Certificate_URL', 'Certificate_start_Month', 'Certificate_start_Year', 'Certificate_End_Month', 'Certificate_End_Year']
        
class CompetitivedetailsForm(forms.ModelForm):
    class Meta:
        model = Competitivedetails
        fields = ['Competitive_Name', 'Competitive_score']
        
class EmploymentDetailsForm(forms.ModelForm):
    class Meta:
        model = EmploymentDetails
        fields = ['Exp_Month', 'Exp_Year', 'Work_Company_Name', 'Work_Designation', 'Work_start_Month', 'Work_start_Year', 'Work_End_Month', 'Work_End_Year', 'Work_Desc']
        
class AwardDetailsForm(forms.ModelForm):
    class Meta:
        model = AwardDetails
        fields = ['work_desc']
        
class AcadmicDetailsForm(forms.ModelForm):
    class Meta:
        model = AcadmicDetails
        fields = ['Acadmic_desc']