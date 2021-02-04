from django.db import models


# Create your models here.
class Experience(models.Model):
    title = models.TextField()
    description = models.TextField()
    year = models.IntegerField()


