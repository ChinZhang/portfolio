from django.contrib import admin
from .models import Project
from .models import ProjectImage
from .models import TopicsLearnedList


# Register your models here.
class ImagesAdmin(admin.StackedInline):
    model = ProjectImage


class ListAdmin(admin.StackedInline):
    model = TopicsLearnedList


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ListAdmin]
    inlines = [ImagesAdmin]

    class Meta:
        model = Project


@admin.register(ProjectImage)
class ImagesAdmin(admin.ModelAdmin):
    pass


@admin.register(TopicsLearnedList)
class ListAdmin(admin.ModelAdmin):
    pass


