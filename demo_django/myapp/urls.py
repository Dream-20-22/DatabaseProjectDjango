from django.urls import path
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.urls import path, include
from . import views

urlpatterns = [

    path('admin1/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('admin/', views.admin, name='admin'),
    path('admin/f1/', views.f1),
    path('admin/f2/', views.f2),
    path('admin/f3/', views.f3),
    path('professor/', views.professor, name='professor'),
    path('professor/f4/', views.f4),
    path('professor/f5/', views.f5),
    path('student/', views.student, name='student'),
    path('student/f6/', views.f6),

]


