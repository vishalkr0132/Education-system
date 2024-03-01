from django.contrib import admin
from .models import *

# Register your models here.

# class ResumesAdmin(admin.ModelAdmin):
#     list_display = ['Student', 'Resume']  # Ensure 'Student' is capitalized

admin.site.register(Resumes)
admin.site.register(ResumeHeadline)
admin.site.register(Educationdata)
admin.site.register(Communication)
admin.site.register(Internshipdetails)
admin.site.register(Projectdetails)
admin.site.register(Certificatedetails)
admin.site.register(Competitivedetails)
admin.site.register(EmploymentDetails)
admin.site.register(AwardDetails)
admin.site.register(AcadmicDetails)
