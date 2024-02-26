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
