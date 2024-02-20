from instructor import views
from django.conf import settings
from django.urls import include,path

urlpatterns = [
    path('instructor_dashboard',views.instructor_dashboard,name='instructor_dashboard'),
    path('admin_instructor_detail',views.admin_instructor_detail,name='admin_instructor_detail'),
]