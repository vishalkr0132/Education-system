from Home import views
from django.conf import settings
from django.urls import include,path
# from .views import logout_view

urlpatterns = [
    path('', views.loginuser, name='sign-in'),
    path('sign_up',views.sign_up,name='sign_up'),
    path('student_sign_in',views.student_sign_in,name='student_sign_in'),
    path('college_sign_in',views.college_sign_in,name='college_sign_in'),
    path('instructor_sign_in',views.instructor_sign_in,name='instructor_sign_in'),
    path('partners_sign_in',views.partners_sign_in,name='partners_sign_in'),
    path('student_sign_up',views.student_sign_up,name='student_sign_up'),
    path('college_sign_up',views.college_sign_up,name='college_sign_up'),
    path('instructor_sign_up',views.instructor_sign_up,name='instructor_sign_up'),
    path('partners_sign_up',views.partners_sign_up,name='partners_sign_up'),
    path('forgot_password',views.forgot_password, name='forgot_password'),
]