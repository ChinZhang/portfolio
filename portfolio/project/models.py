from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.TextField()
    description = models.TextField()
    technology = models.TextField()
    date = models.IntegerField()

