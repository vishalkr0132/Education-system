from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class signup(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    User_Type = models.CharField(max_length=255)
    First_Name = models.CharField(max_length=255)
    Last_Name = models.CharField(max_length=255, null=True)
    Mobile = models.CharField(max_length=10)
    Email = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    Confirm_Password = models.CharField(max_length=255)
    
    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(signup, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.Email