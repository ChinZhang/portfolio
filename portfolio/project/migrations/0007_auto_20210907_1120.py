# Generated by Django 3.1.4 on 2021-09-07 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_auto_20210907_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='static/resources/project_images'),
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='images',
            field=models.ImageField(default='', upload_to='static/resources/project_images'),
        ),
    ]
