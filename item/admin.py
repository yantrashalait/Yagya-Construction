from django.contrib import admin
from . models import HomepageImage, Organization, SolutionPage, ProcessPage, ProcessStep, Service, Project, ProjectImage, AboutUs, ContactDetail, Message, SolutionWeProvide

# Register your models here.
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 2

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ ProjectImageInline, ]

admin.site.register(Project, ProjectAdmin)
admin.site.register(HomepageImage)
admin.site.register(Organization)
admin.site.register(SolutionPage)
admin.site.register(ProcessPage)
admin.site.register(ProcessStep)
admin.site.register(Service)
admin.site.register(AboutUs)
admin.site.register(ContactDetail)
admin.site.register(Message)
admin.site.register(SolutionWeProvide)
