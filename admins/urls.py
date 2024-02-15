from admins import views
from django.conf import settings
from django.urls import include,path
from .views import logout_view

urlpatterns = [
    path('', views.loginuser, name='sign-in'),
    path('sign_up',views.sign_up,name='sign_up'),
    path('forgot_password',views.forgot_password, name='forgot_password'),
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('admin_instructor_detail',views.admin_instructor_detail, name='admin_instructor_detail'),
    path('admin_instructor_list',views.admin_instructor_list, name='admin_instructor_list'),
    path('admin_instructor_request',views.admin_instructor_request, name='admin_instructor_request'),
    path('admin_student_list',views.admin_student_list, name='admin_student_list'),
    path('admin_course_list',views.admin_course_list, name='admin_course_list'),
    path("admin_course_category",views.admin_course_category, name='admin_course_category'),
    path('admin_course_detail',views.admin_course_detail, name='admin_course_detail'),
    path('logout/', logout_view, name='logout'),
    
]