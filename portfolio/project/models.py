from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.TextField()
    technology = models.TextField(default='')
    year = models.IntegerField(default='')
    image = models.ImageField(blank=True, default='', upload_to='static/resources/project_images')
    description = models.TextField(default='')
    experience = models.TextField(default='')
    improvements = models.TextField(default='')
    reflection = models.TextField(default='')
    github_link = models.URLField(blank=True)
    project_link = models.URLField(blank=True)
    github_icon = models.TextField(blank=True)
    disclaimer = models.TextField(blank=True)
    class_event = models.TextField(blank=True)
    role = models.TextField(blank=True)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='static/resources/project_images', default='')

    def __str__(self):
        return self.project.title


class TopicsLearnedList(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    topics = models.TextField(default='')

    def __str__(self):
        return self.project.title
