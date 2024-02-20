from django.contrib import admin
from .models import students_sign_up,colleges_sign_up,instructors_sign_up

# Register your models here.

admin.site.register(students_sign_up),
admin.site.register(colleges_sign_up),
admin.site.register(instructors_sign_up),
