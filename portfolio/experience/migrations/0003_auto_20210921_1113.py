# Generated by Django 3.1.4 on 2021-09-21 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0002_auto_20210203_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='company',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='date_range',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='experience',
            name='icon',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='experience',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='experience',
            name='title',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='experience',
            name='year',
            field=models.IntegerField(default=''),
        ),
    ]
