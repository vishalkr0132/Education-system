from django.db import models
from django.contrib.auth.models import User
from Home.models import students_sign_up

# Create your models here.
# class Profiles(models.Model):
#     Student = models.OneToOneField(students_sign_up, on_delete=models.CASCADE)
#     Profile_Pic = models.ImageField(upload_to='profiles/', null=True, blank=True)
#     First_Name = models.CharField(max_length=255)
#     Last_Name = models.CharField(max_length=255)
#     Email = models.CharField(max_length=255)
#     Location = models.CharField(max_length=255, null=True, blank=True)
#     Phone = models.CharField(max_length=20, null=True, blank=True)
#     Gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], null=True, blank=True)
#     DOB = models.DateField(null=True, blank=True)
#     about = models.TextField(null=True, blank=True)

#     def save(self, *args, **kwargs):
#         super(Profiles, self).save(*args, **kwargs)
#         self.Student.First_Name = self.First_Name
#         self.Student.Last_Name = self.Last_Name
#         self.Student.Email = self.Email
#         self.Student.save()

#     def __str__(self):
#         return self.First_Name + ' ' + self.Last_Name

# class Resumes(models.Model):
#     Student = models.OneToOneField(students_sign_up, on_delete=models.CASCADE, related_name='resume')
#     Resume = models.FileField(upload_to='Resumes/')

#     def __str__(self):
#         return f"Resume of {self.student.email}"
class Resumes(models.Model):
    id = models.AutoField(primary_key=True)
    # user = models.OneToOneField(User, related_name='resume', on_delete=models.CASCADE)
    Resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.id
