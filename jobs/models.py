from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.text import slugify

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    location = models.CharField(max_length=100)
    availability = models.CharField(max_length=100, default="Freelance / Full-time")
    tagline = models.TextField()
    bio = models.TextField()
    professions = models.CharField(max_length=255, help_text="Comma-separated list of professions for the typing animation")
    github_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    resume = CloudinaryField(resource_type='raw', blank=True, null=True, help_text="Upload your resume PDF to Cloudinary")
    profile_photo = CloudinaryField('image', blank=True, null=True)

    def get_resume_url(self):
        if self.resume:
            val = str(self.resume)
            if "http" in val or val.startswith("/"):
                return val
            try:
                return self.resume.url
            except Exception:
                return f"https://res.cloudinary.com/zumkibja/raw/upload/{val}"
        return ""

    def get_photo_url(self):
        if self.profile_photo:
            val = str(self.profile_photo)
            if "http" in val:
                return val
            if val == "irhy0v8xivjrm3nu2qlk":
                return "https://res.cloudinary.com/zkmuak5b/image/upload/v1783450680/irhy0v8xivjrm3nu2qlk.jpg"
            try:
                return self.profile_photo.url
            except Exception:
                return f"https://res.cloudinary.com/zumkibja/image/upload/{val}"
        return ""

    def __str__(self):
        return self.name


class skills(models.Model):
    skill = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100, default="fa-solid fa-code", help_text="FontAwesome icon class (e.g. 'fa-brands fa-python')")

    def __str__(self):
        return self.skill


class Job(models.Model):
    image = CloudinaryField('image')
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, max_length=150)
    summary = models.CharField(max_length=500)
    overview = models.TextField(blank=True)
    features = models.TextField(blank=True, help_text="One feature per line")
    challenges = models.TextField(blank=True, help_text="One challenge/solution per line")
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    technologies = models.ManyToManyField(skills, blank=True, related_name='jobs')
    is_featured = models.BooleanField(default=False)
    status = models.CharField(max_length=50, default="Completed", choices=[("Completed", "Completed"), ("In Progress", "In Progress")])
    published_date = models.CharField(max_length=50, default="June 2026")
    order = models.PositiveIntegerField(default=0, help_text="Order in which projects are displayed")

    class Meta:
        ordering = ['order', 'id']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_image_url(self):
        if self.image:
            val = str(self.image)
            if "http" in val:
                return val
            ref_mappings = {
                "utzmlnrhgcw5npl7my0t": "https://res.cloudinary.com/zkmuak5b/image/upload/v1783369165/utzmlnrhgcw5npl7my0t.png",
                "mcvnxll9bsvthwemgzde": "https://res.cloudinary.com/zkmuak5b/image/upload/v1783456671/mcvnxll9bsvthwemgzde.png",
                "frx7txyls0ls5ljybkor": "https://res.cloudinary.com/zkmuak5b/image/upload/v1783370481/frx7txyls0ls5ljybkor.webp",
            }
            if val in ref_mappings:
                return ref_mappings[val]
            try:
                return self.image.url
            except Exception:
                return f"https://res.cloudinary.com/zumkibja/image/upload/{val}"
        return ""

    def __str__(self):
        return self.title


class ProjectGalleryImage(models.Model):
    project = models.ForeignKey(Job, related_name='gallery_images', on_delete=models.CASCADE)
    image = CloudinaryField('image')
    caption = models.CharField(max_length=100, blank=True)

    def get_image_url(self):
        if self.image:
            val = str(self.image)
            if "http" in val:
                return val
            ref_mappings = {
                "d7gkgelyxyrv2wx9kich": "https://res.cloudinary.com/zkmuak5b/image/upload/v1783455154/d7gkgelyxyrv2wx9kich.png",
                "thvbbfozwgj8vllhgzyu": "https://res.cloudinary.com/zkmuak5b/image/upload/v1783455155/thvbbfozwgj8vllhgzyu.png",
                "xu3whui0gywf3s8qiqgy": "https://res.cloudinary.com/zkmuak5b/image/upload/v1783455156/xu3whui0gywf3s8qiqgy.png",
                "zd0samuxfldacy18zvhq": "https://res.cloudinary.com/zkmuak5b/image/upload/v1783455156/zd0samuxfldacy18zvhq.png",
                "c9lhchooybbgct152pup": "https://res.cloudinary.com/zkmuak5b/image/upload/v1783455157/c9lhchooybbgct152pup.png",
                "ip5evqoeflvc2cg9ifjm": "https://res.cloudinary.com/zkmuak5b/image/upload/v1783455158/ip5evqoeflvc2cg9ifjm.png",
            }
            if val in ref_mappings:
                return ref_mappings[val]
            try:
                return self.image.url
            except Exception:
                return f"https://res.cloudinary.com/zumkibja/image/upload/{val}"
        return ""

    def __str__(self):
        return f"Gallery Image for {self.project.title}"


class Experience(models.Model):
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50, default="Present")
    description = models.TextField()
    technologies = models.ManyToManyField(skills, blank=True, related_name='experiences')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.role} at {self.company}"


class Education(models.Model):
    degree = models.CharField(max_length=150)
    college = models.CharField(max_length=150)
    date_range = models.CharField(max_length=50)
    cgpa = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.degree


class Certificate(models.Model):
    title = models.CharField(max_length=150)
    organization = models.CharField(max_length=150)
    year = models.CharField(max_length=50)
    verification_link = models.URLField(blank=True, null=True)
    credential_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

   