from instructor import views
from django.conf import settings
from django.urls import include,path
from .views import logout_view

urlpatterns = [
    path('',views.instructor_dashboard,name='instructor_dashboard'),
    path('admin_instructor_detail',views.admin_instructor_detail,name='admin_instructor_detail'),
    path('logout/', logout_view, name='logout'),
]
