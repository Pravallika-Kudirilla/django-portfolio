from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Job(models.Model):
    image = CloudinaryField('image')
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=200)
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)

    def __str__(self):
        return self.title