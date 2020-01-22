from django.db import models
from django.utils import timezone


class ProjectOverView(models.Model):
    heading = models.TextField()
    description = models.TextField()

    class Meta:
        verbose_name = "1. Project Page Content"


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

    class Meta:
        verbose_name = "2. Project"


class ProjectImage(models.Model):
    image = models.ImageField(upload_to='project/', help_text="Image size: width: 900px height: 879px")
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE, null=True, blank=True)
