from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.TextField()
    description = models.TextField()
    technology = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()

