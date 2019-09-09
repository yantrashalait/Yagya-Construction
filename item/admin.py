from django.contrib import admin
from . models import Index, Organization, Solution, ProcessMain, Process, Service, Project, ProjectImage, About, Contact, ContactForm

# Register your models here.
admin.site.register(Index)
admin.site.register(Organization)
admin.site.register(Solution)
admin.site.register(ProcessMain)
admin.site.register(Process)
admin.site.register(Service)
admin.site.register(Project)
admin.site.register(ProjectImage)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(ContactForm)