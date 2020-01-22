from django.db import models
from django.utils import timezone

# Create your models here.
class HomepageImage(models.Model):
    image = models.ImageField(upload_to='index/', help_text="Image size: width=1220px height=927px")
