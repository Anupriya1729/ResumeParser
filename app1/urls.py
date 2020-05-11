from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home,name='app1-home'),
    path('uploadpage/', views.uploadpage, name='app1-uploadpage'),
    path('uploadnow/', views.uploadnow, name='app1-uploadnow'),
    path('success/', views.success, name='app1-success'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
