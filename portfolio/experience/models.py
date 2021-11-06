from django.db import models


# Create your models here.
class Experience(models.Model):
    title = models.TextField(default='')
    company = models.TextField(blank=True)
    location = models.TextField(default='')
    link = models.URLField(default='')
    description = models.TextField(default=True)
    date_range = models.TextField(default='')
    icon = models.TextField(default='')
    year = models.IntegerField(default='')


