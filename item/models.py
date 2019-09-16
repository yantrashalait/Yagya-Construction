from django.db import models
from django.utils import timezone

# Create your models here.
class HomepageImage(models.Model):
    image = models.ImageField(upload_to='index/', help_text="Image size: width=193px height=115px")

class Organization(models.Model):
    organization_name = models.CharField(max_length=100, null=True, blank=True)
    organization_address = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    organization_heading = models.TextField()
    description = models.TextField()
    company_slogan = models.CharField(max_length=500, null=True, blank=True) 

class SolutionPage(models.Model):
    main_image = models.ImageField(upload_to='solution/', help_text="Image size: width=193px height=115px")
    title = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class ProcessPage(models.Model):
    main_image = models.ImageField(upload_to='process/', help_text="Image size: width=193px height=115px")
    title = models.TextField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class ProcessStep(models.Model):
    step_name = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='process/')
    step_description = models.TextField()

    def __str__(self):
        return self.step_name

class Service(models.Model):
    service_name = models.TextField(null=True, blank=True)
    icon = models.ImageField(upload_to='process/')
    description = models.TextField()
    
    def __str__(self):
        return self.service_name


PROJECT_TYPES = (
    (1, "Upcoming"),
    (2, "Ongoing"),
    (3, "Completed"),
)


class Project(models.Model):
    project_name = models.TextField(null=True, blank=True)
    project_description = models.TextField()
    client_name = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    sector = models.CharField(max_length=100, null=True, blank=True)
    project_status = models.IntegerField(choices=PROJECT_TYPES, null=True, blank=True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.project_name

class ProjectImage(models.Model):
    image = models.ImageField(upload_to='project/')
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE, null=True, blank=True)
    
class AboutUs(models.Model):
    title = models.TextField(null=True, blank=True)
    main_image = models.ImageField(upload_to='about/')
    secondary_image = models.ImageField(upload_to='about/')
    video_url = models.URLField(help_text="Please enter the url of the video from youtube or other sources")
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class ContactDetail(models.Model):
    contact_title = models.TextField(help_text="Example: For a project, as a partner or as a team.")
    contact_description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='contact/')

class Message(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    number = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    message =  models.TextField()

class SolutionWeProvide(models.Model):
    solution_name = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='solution/')

class ProjectOverView(models.Model):
    heading = models.TextField()
    description = models.TextField()