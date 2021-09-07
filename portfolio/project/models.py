from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.TextField()
    description = models.TextField(default='')
    experience = models.TextField(default='')
    link = models.URLField(blank=True)
    technology = models.TextField(default='')
    year = models.IntegerField(default='')
    image = models.ImageField(blank=True, default='', upload_to='static/resources/project_images')

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='static/resources/project_images', default='')

    def __str__(self):
        return self.project.title

