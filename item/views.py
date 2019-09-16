from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from . models import HomepageImage, ProcessPage, AboutUs, ContactDetail, Organization, ProcessStep, Message, SolutionPage, Service, Project, ProjectImage, ProjectOverView, SolutionWeProvide
from . forms import ContactForm
# Create your views here.

class ContactView(TemplateView):
    template_name = 'item/contact.html'
    model = ContactDetail
    form_class = ContactForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = ContactDetail.objects.first()
        return context

    def post(self, request, *args, **kwargs):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        address = request.POST.get('address')
        company_name = request.POST.get('company_name')
        message = request.POST.get('message')

        success = Message.objects.create(first_name=first_name, last_name=last_name, email=email, number=number, address=address, company_name=company_name, message=message)

        return HttpResponseRedirect('/')

class ProjectView(TemplateView):
    template_name = 'item/projects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = Project.objects.all() 
        return context

class IndexView(TemplateView):
    template_name = 'item/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['index'] = HomepageImage.objects.first() 
        context['organization'] = Organization.objects.first() 
        context['projects'] = Project.objects.filter(project_status=2)
        context['project_overview'] = ProjectOverView.objects.first()
        return context

class AboutView(TemplateView):
    template_name = 'item/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = AboutUs.objects.first() 
        return context

class ProcessView(TemplateView):
    template_name = 'item/process.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['process'] = ProcessPage.objects.first() 
        context['process_down'] = ProcessStep.objects.all()
        return context

class SolutionView(TemplateView):
    template_name = 'item/solutions.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['solution'] = SolutionPage.objects.first() 
        context['service'] = Service.objects.all()
        context['solution_provide'] = SolutionWeProvide.objects.all()
        return context
