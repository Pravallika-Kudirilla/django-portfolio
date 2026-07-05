from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),  
    path('jobs/<int:job_id>',views.detail,name='detail'),
    path('create-admin/', views.create_admin, name='create_admin'), 
]