from django.contrib import admin
from .models import Resumes

# Register your models here.

# class ResumesAdmin(admin.ModelAdmin):
#     list_display = ['Student', 'Resume']  # Ensure 'Student' is capitalized

admin.site.register(Resumes)
