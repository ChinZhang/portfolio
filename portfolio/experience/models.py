from django.db import models


# Create your models here.
class Experience(models.Model):
    title = models.TextField(default='')
    company = models.TextField(blank=True)
    location = models.TextField(default='')
    type = models.TextField(blank=True)
    link = models.URLField(default='')
    description = models.TextField(blank=True)
    date_range = models.TextField(default='')
    icon = models.TextField(default='')
    year = models.IntegerField(default='')


