from django.db import models

class SolutionPage(models.Model):
    main_image = models.ImageField(upload_to='solution/', help_text="Image size: width=1220px height=711px")
    title = models.TextField(null=True, blank=True)
    heading = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "1. Solution Page"


class SolutionWeProvide(models.Model):
    solution_name = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='solution/', help_text="Image size: width=711px height=410px")

    def __str__(self):
        return self.solution_name

    class Meta:
        verbose_name = "2. Solution We Provide"


class Service(models.Model):
    service_name = models.TextField(null=True, blank=True)
    icon = models.ImageField(upload_to='process/', help_text="Image size: width=71px height=68px")
    description = models.TextField()
    
    def __str__(self):
        return self.service_name

    class Meta:
        verbose_name = "3. Service"
