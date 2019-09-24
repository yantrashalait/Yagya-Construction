from .models import Project, Organization

def footer_processor(request):
    project = Project.objects.all()
    organization = Organization.objects.first()
    context = {'project': project,
               'organization': organization,
               }

    return context