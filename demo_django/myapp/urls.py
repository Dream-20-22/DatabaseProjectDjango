from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('admin/', views.admin, name='admin'),
    path('admin/f1/', views.f1),
    path('admin/f2/', views.f2),
    path('admin/f3/', views.f3),
    path('professor/', views.professor, name='professor'),
    path('professor/courses/', views.professorCourses),
    path('professor/students/', views.professorStudents),
    path('student/', views.student, name='student'),
    path('student/studentCourses/', views.studentCourses),

]
