from django.db import models


# Create your models here.
class Experience(models.Model):
    title = models.TextField(default='')
    company = models.TextField(blank=True)
    description = models.TextField(default='')
    date_range = models.TextField(default='')
    icon = models.TextField(default='')
    year = models.IntegerField(default='')


