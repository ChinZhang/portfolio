# Generated by Django 3.1.4 on 2021-09-07 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20210907_1010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectimage',
            name='image',
        ),
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='projectimage',
            name='images',
            field=models.ImageField(default='', upload_to='resources/'),
        ),
    ]