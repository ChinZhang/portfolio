# Generated by Django 3.1.4 on 2021-11-03 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_project_class_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='role',
            field=models.TextField(blank=True),
        ),
    ]
