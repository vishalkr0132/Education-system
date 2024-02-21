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
    path('student_profile', views.student_profile, name='student_profile')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)