# Generated by Django 3.1.4 on 2021-11-06 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0006_auto_20211105_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
