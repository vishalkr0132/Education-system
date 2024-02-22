from django.db import models
from Home.models import students_sign_up

# Create your models here.
# # Resume upload
# class Resume(models.Model):
#     id = models.AutoField(primary_key=True)
#     user = models.ForeignKey(students_sign_up, related_name='resumes', on_delete=models.CASCADE)
#     cv = models.FileField(upload_to='resumes/')

# # Resume headline
# class Resumeheadline(models.Model):
#     user = models.AutoField(primary_key=True)
#     # user = models.OneToOneField(students_sign_up, on_delete=models.CASCADE)
#     headline = models.TextField()

#     def __str__(self):
#         return self.headline

# # Education based
# class EducationDetail(models.Model):
#     id = models.AutoField(primary_key=True)
#     user = models.OneToOneField(students_sign_up, on_delete=models.CASCADE)
#     college = models.CharField(max_length=255)
#     start_year = models.IntegerField()
#     end_year = models.IntegerField()
#     degree = models.CharField(max_length=100)
#     stream = models.CharField(max_length=100)
#     grading_system = models.CharField(max_length=10)
#     performance = models.CharField(max_length=20)
#     course_type = models.CharField(max_length=20)
    
# # IT skills
# # we will update soon


# # Languages 
# class Languages(models.Model):
#     id = models.AutoField(primary_key=True)
#     user = models.OneToOneField(students_sign_up, on_delete=models.CASCADE)
#     languages_toungh = models.CharField(max_length=20)