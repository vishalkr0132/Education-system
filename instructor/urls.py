from instructor import views
from django.conf import settings
from django.urls import include,path
from .views import logout_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.instructor_dashboard,name='instructor_dashboard'),
    path('admin_instructor_detail',views.admin_instructor_detail,name='admin_instructor_detail'),
    path('logout/', logout_view, name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
