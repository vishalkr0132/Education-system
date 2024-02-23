from django.shortcuts import render
from django.shortcuts import redirect,render,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from Home.models import students_sign_up
from django.contrib import messages
from django.http import FileResponse
from django.core.files.storage import default_storage
from django.http import Http404


# Create your views here.
def student_dashboard(request):
    if request.user.is_anonymous:
        return redirect('/')
    else:
        username = request.user.username
        Student = students_sign_up.objects.filter(Email=username)
        context = {'Student': Student}
        return render(request, 'student-dashboard.html', context)

def student_profile(request):
    return render(request, 'student-profile.html')

def logout_view(request):
    logout(request)
    return redirect('/')