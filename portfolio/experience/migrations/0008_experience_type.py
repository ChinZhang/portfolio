# Generated by Django 3.1.4 on 2021-11-06 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0007_auto_20211105_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='type',
            field=models.TextField(blank=True),
        ),
    ]
