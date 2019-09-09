from django.db import models
from django.utils import timezone

# Create your models here.
class Index(models.Model):
    title = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='index/', help_text="Image size: width=193px height=115px")
    description = models.TextField()
    slogan = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

class Organization(models.Model):
    description1 = models.TextField()
    description2 = models.TextField()
    slogan = models.CharField(max_length=100, null=True, blank=True)

class Solution(models.Model):
    main_image = models.ImageField(upload_to='solution/', help_text="Image size: width=193px height=115px")
    title = models.TextField(null=True, blank=True)
    description1 = models.TextField()
    description2 = models.TextField()

    def __str__(self):
        return self.title

class ProcessMain(models.Model):
    main_image = models.ImageField(upload_to='process/', help_text="Image size: width=193px height=115px")
    title = models.TextField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class Process(models.Model):
    title = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='process/')
    description = models.TextField()

    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.TextField(null=True, blank=True)
    icon = models.ImageField(upload_to='process/')
    description = models.TextField()
    
    def __str__(self):
        return self.title


PROJECT_TYPES = (
    (1, "Upcoming"),
    (2, "Ongoing"),
    (3, "Completed"),
)


class Project(models.Model):
    title = models.TextField(null=True, blank=True)
    description = models.TextField()
    client_name = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    sector = models.CharField(max_length=100, null=True, blank=True)
    project_type = models.IntegerField(choices=PROJECT_TYPES, null=True, blank=True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    image = models.ImageField(upload_to='project/')
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE, null=True, blank=True)
    
class About(models.Model):
    title = models.TextField(null=True, blank=True)
    main_image = models.ImageField(upload_to='about/')
    secondary_image = models.ImageField(upload_to='about/')
    video = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    slogan = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    image = models.ImageField(upload_to='contact/')

class ContactForm(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    number = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    message =  models.TextField()
