from django.db import models

class Organization(models.Model):
    organization_name = models.CharField(max_length=100, null=True, blank=True)
    organization_address = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    organization_heading = models.TextField()
    description = models.TextField()
    company_slogan = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.organization_name
    
    class Meta:
        verbose_name = "2. Organization Detail"

    
class AboutUs(models.Model):
    title = models.TextField(null=True, blank=True)
    main_image = models.ImageField(upload_to='about/', help_text="Image size: width: 1422px height: 711px")
    secondary_image = models.ImageField(upload_to='about/', help_text="Image size: width=585px height=342px")
    thumbnail_image = models.ImageField(upload_to='thumbnail/', help_text="Image size: width=840px height=558px")
    video_url = models.URLField(help_text="Please enter the url of the video from youtube or other sources")
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "1. About Us Page Content"
