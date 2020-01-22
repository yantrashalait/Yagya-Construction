from django.db import models

class ProcessPage(models.Model):
    main_image = models.ImageField(upload_to='process/', help_text="Image size: width=1885px height=931px")
    title = models.TextField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "1. Process Page Content"

class ProcessStep(models.Model):
    step_name = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='process/', help_text="Image size: width=289px height=296px")
    step_description = models.TextField()

    def __str__(self):
        return self.step_name

    class Meta:
        verbose_name = "2. Process Step"