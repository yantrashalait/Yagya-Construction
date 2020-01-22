from django.db import models


class ContactDetail(models.Model):
    contact_title = models.TextField(help_text="Example: For a project, as a partner or as a team.")
    contact_description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='contact/', help_text="Image size: width: 1422px height: 711px")

    def __str__(self):
        return self.contact_title

    class Meta:
        verbose_name = "1. Contact Us Page Content"


class Message(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    number = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    message =  models.TextField()

    class Meta:
        verbose_name = "2. (Not for inserting data) User's Message"

    def __str__(self):
        return self.first_name + ' ' + self.last_name