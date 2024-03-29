# Generated by Django 3.1.4 on 2021-09-07 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20210907_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='experience',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='technology',
            field=models.TextField(default=''),
        ),
    ]
