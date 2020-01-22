from aboutus_page.models import Organization
from project_page.models import Project

def footer_processor(request):
    project = Project.objects.all()
    organization = Organization.objects.first()
    context = {'project': project,
               'organization': organization,
               }

    return context