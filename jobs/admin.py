from django.contrib import admin
from .models import Profile, skills, Job, ProjectGalleryImage, Experience, Education, Certificate

class ProjectGalleryImageInline(admin.TabularInline):
    model = ProjectGalleryImage
    extra = 1

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectGalleryImageInline]
    list_display = ('title', 'order', 'status', 'is_featured')
    list_editable = ('order',)

admin.site.register(Profile)
admin.site.register(skills)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Certificate)