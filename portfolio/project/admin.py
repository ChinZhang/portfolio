from django.contrib import admin
from .models import Project
from .models import ProjectImage


# Register your models here.
class ImagesAdmin(admin.StackedInline):
    model = ProjectImage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ImagesAdmin]

    class Meta:
        model = Project


@admin.register(ProjectImage)
class ImagesAdmin(admin.ModelAdmin):
    pass


