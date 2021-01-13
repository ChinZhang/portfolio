from django.db import models


# Create your models here.
class Experience(models.Model):
    title = models.TextField()
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()


