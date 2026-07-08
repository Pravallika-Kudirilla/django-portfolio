from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('projects/', views.projects_list, name='projects_list'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('certificates/', views.certificates_list, name='certificates_list'),
    path('jobs/<int:job_id>/', views.detail, name='detail'),
    path('create-admin/', views.create_admin, name='create_admin'), 
]