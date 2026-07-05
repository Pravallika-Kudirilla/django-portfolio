from django.shortcuts import render,get_object_or_404
from .models import Job 
from django.contrib.auth.models import User
from django.http import HttpResponse

def home(request):
    jobs=Job.objects.all()

    return render(
        request,'jobs/home.html',{'jobs':jobs},
         )


def detail(request,job_id):
    job=get_object_or_404(Job,pk=job_id)
    return render(request,'jobs/detail.html',{'job':job})

def create_admin(request):
    username = "admin"

    if User.objects.filter(username=username).exists():
        return HttpResponse("Admin already exists!")

    User.objects.create_superuser(
        username="admin",
        email="pravallikakudirilla77@gmail.com",
        password="Admin@123"
    )

    return HttpResponse("Admin created successfully!")