from django.contrib import admin
from .models import Project, ProjectImage, ProjectOverView

# Register your models here.
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 2

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ ProjectImageInline, ]

admin.site.register(ProjectOverView)
admin.site.register(Project, ProjectAdmin)
