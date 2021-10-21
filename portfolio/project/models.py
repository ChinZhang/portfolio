from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.TextField()
    description = models.TextField(default='')
    experience = models.TextField(default='')
    github_link = models.URLField(blank=True)
    project_link = models.URLField(blank=True)
    github_icon = models.TextField(blank=True)
    disclaimer = models.TextField(blank=True)
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

