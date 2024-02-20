from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class students_sign_up(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    First_Name = models.CharField(max_length=255)
    Last_Name = models.CharField(max_length=255, null=True)
    Email = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    
    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(students_sign_up, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.Email
    
class colleges_sign_up(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    College_Name = models.CharField(max_length=255)
    College_Code = models.CharField(max_length=255)
    Admin_Administrator = models.CharField(max_length=255)
    Phone = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255)
    Password = models.CharField(max_length=255)
    
    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(colleges_sign_up, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.Email
    