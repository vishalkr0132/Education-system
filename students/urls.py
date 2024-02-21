from students import views
# from admins import views
from django.conf import settings
from django.urls import include,path
from .views import logout_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('', views.student_dashboard, name='student_dashboard'),
    path('admin_student_list', views.admin_student_list, name='admin_student_list'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)