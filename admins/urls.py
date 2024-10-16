from admins import views
from django.conf import settings
from django.urls import include,path
from .views import logout_view
from django.conf.urls.static import static


urlpatterns = [
    path('',views.admin_dashboard,name='admin_dashboard'),
    path('admin_profile',views.admin_profile,name='profile'),
    path('admin_instructor_detail',views.admin_instructor_detail, name='admin_instructor_detail'),
    path('admin_instructor_list',views.admin_instructor_list, name='admin_instructor_list'),
    path('admin_instructor_request',views.admin_instructor_request, name='admin_instructor_request'),
    path('admin_student_list',views.admin_student_list, name='admin_student_list'),
    path('admin_college_list',views.admin_college_list, name='admin_college_list'),
    path('admin_student_detail/<int:Pid>',views.admin_student_detail, name='admin_student_detail'),
    path('admin_course_list',views.admin_course_list, name='admin_course_list'),
    path("admin_course_category",views.admin_course_category, name='admin_course_category'),
    path('admin_course_detail',views.admin_course_detail, name='admin_course_detail'),
    path('instructor_create_course',views.instructor_create_course, name='instructor_create_course'),
    path('admin_edit_course_detail',views.admin_edit_course_detail, name='admin_edit_course_detail'),
    path('logout/', logout_view, name='logout'),
    path('activate/<int:PID>', views.activate, name="activate"),
    path('rejecct/<int:PID>', views.reject, name="reject"),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)