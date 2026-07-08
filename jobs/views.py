from django.shortcuts import render, get_object_or_404, redirect
from .models import Job, skills, Profile, ProjectGalleryImage, Experience, Education, Certificate
from django.contrib.auth.models import User
from django.http import HttpResponse

def home(request):
    profile = Profile.objects.first()
    skill_list = skills.objects.all()
    jobs = Job.objects.all()
    experiences = Experience.objects.all()
    education = Education.objects.all()
    certificates = Certificate.objects.all()
    return render(request, 'jobs/home.html', {
        'profile': profile,
        'skills': skill_list,
        'jobs': jobs,
        'experiences': experiences,
        'education': education,
        'certificates': certificates,
    })

def projects_list(request):
    jobs = Job.objects.all()
    profile = Profile.objects.first()
    all_skills = skills.objects.all()
    return render(request, 'jobs/project_list.html', {
        'jobs': jobs,
        'profile': profile,
        'skills': all_skills,
    })

def project_detail(request, slug):
    job = get_object_or_404(Job, slug=slug)
    profile = Profile.objects.first()
    
    # Get previous and next project for navigation
    jobs_list = list(Job.objects.order_by('id'))
    try:
        idx = jobs_list.index(job)
        prev_job = jobs_list[idx - 1] if idx > 0 else None
        next_job = jobs_list[idx + 1] if idx < len(jobs_list) - 1 else None
    except ValueError:
        prev_job = None
        next_job = None
        
    related_jobs = Job.objects.exclude(id=job.id)[:2]
    
    # Process features and challenges (split by newline for template list rendering)
    features_list = [f.strip() for f in job.features.split('\n') if f.strip()]
    challenges_list = [c.strip() for c in job.challenges.split('\n') if c.strip()]
    
    return render(request, 'jobs/project_detail.html', {
        'job': job,
        'profile': profile,
        'prev_job': prev_job,
        'next_job': next_job,
        'related_jobs': related_jobs,
        'features_list': features_list,
        'challenges_list': challenges_list,
    })

def certificates_list(request):
    certificates = Certificate.objects.all()
    profile = Profile.objects.first()
    return render(request, 'jobs/certificate_list.html', {
        'certificates': certificates,
        'profile': profile,
    })

def detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return redirect('project_detail', slug=job.slug)

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