from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home,name='app-home'),
    path('uploadpage/', views.uploadpage, name='app-uploadpage'),
    path('upload/', views.upload, name='app-upload'),
    path('success/', views.success, name='app-success'),
   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
