from admins import views
from django.conf import settings
from django.urls import include,path
from .views import logout_view

urlpatterns = [
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('admin_instructor_detail',views.admin_instructor_detail, name='admin_instructor_detail'),
    path('admin_instructor_list',views.admin_instructor_list, name='admin_instructor_list'),
    path('admin_instructor_request',views.admin_instructor_request, name='admin_instructor_request'),
    path('admin_student_list',views.admin_student_list, name='admin_student_list'),
    path('admin_course_list',views.admin_course_list, name='admin_course_list'),
    path("admin_course_category",views.admin_course_category, name='admin_course_category'),
    path('admin_course_detail',views.admin_course_detail, name='admin_course_detail'),
    path('instructor_create_course',views.instructor_create_course, name='instructor_create_course'),
    path('admin_edit_course_detail',views.admin_edit_course_detail, name='admin_edit_course_detail'),
    path('logout/', logout_view, name='logout'),
    
]