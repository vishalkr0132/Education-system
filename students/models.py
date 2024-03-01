from django.db import models
from django.contrib.auth.models import User
from Home.models import students_sign_up

# Create your models here.

class Resumes(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    user = models.OneToOneField(User, related_name='resume', on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    
    def __str__(self):
            return f"Resume of {self.user.email}"
        
class ResumeHeadline(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Resume_headline_data = models.TextField()
    
    def __str__(self):
        return self.Resume_headline_data

class Educationdata(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    College_Name = models.CharField( max_length=255)
    College_Start_Year = models.IntegerField()
    College_End_Year = models.IntegerField()
    Degree = models.CharField(max_length=100)
    Stream = models.CharField(max_length=100)
    Grading_System = models.CharField(max_length=10)
    Performance = models.CharField(max_length=20)
    Course_Type = models.CharField(max_length=20)
    
    def __str__(self):
        return f"Education data {self.user.email}"
    
class Communication(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Communication_Language = models.CharField(max_length=30)
    
    def __str__(self):
        return f"Language {self.user.email}"
    
class Internshipdetails(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Intern_Company_Name = models.CharField(max_length=150)
    Intern_Start_Month = models.CharField(max_length=100)
    Intern_Start_Year = models.IntegerField()
    Intern_End_Month = models.CharField(max_length=100)
    Intern_End_Year = models.IntegerField()
    Intern_Project_Name = models.CharField(max_length=255)
    Intern_Desc = models.TextField()
    Intern_Project_Url = models.CharField(max_length=150)
    
    def __str__(self):
        return f"Intern {self.user.email}"
    
class Projectdetails(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Project_Name = models.CharField(max_length=150)
    Project_Start_Month = models.CharField(max_length=100)
    Project_Start_Year = models.IntegerField()
    Project_End_Month = models.CharField(max_length=100)
    Project_End_Year = models.IntegerField()
    Project_Desc = models.TextField()
    Project_Url = models.CharField(max_length=150)
    
    def __str__(self):
        return f"Project {self.user.email}"

class Certificatedetails(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Certificate_Name = models.CharField(max_length=150)
    Certificate_ID = models.CharField(max_length=100)
    Certificate_URL = models.CharField(max_length=100)
    Certificate_start_Month = models.CharField(max_length=100)
    Certificate_start_Year = models.IntegerField()
    Certificate_End_Month = models.CharField(max_length=100)
    Certificate_End_Year = models.IntegerField()
    
    def __str__(self):
        return f"Certificate {self.user.email}"

class Competitivedetails(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Competitive_Name = models.CharField(max_length=150)
    Competitive_score = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Competitive {self.user.email}"
    
class EmploymentDetails(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Exp_Year = models.IntegerField()
    Exp_Month = models.CharField(max_length=100)
    Work_Company_Name = models.CharField(max_length=150)
    Work_Designation = models.CharField(max_length=100)
    Work_start_Month = models.CharField(max_length=100)
    Work_start_Year = models.IntegerField()
    Work_End_Month = models.CharField(max_length=100)
    Work_End_Year = models.IntegerField()
    Work_Desc = models.TextField()
    
    
    def __str__(self):
        return f"Certificate {self.user.email}"
    
class AwardDetails(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    work_desc = models.TextField()

    def __str__(self):
        return f"Award for {self.user.email}"
    
class AcadmicDetails(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Acadmic_desc = models.TextField()

    def __str__(self):
        return f"Acadmic for {self.user.email}"