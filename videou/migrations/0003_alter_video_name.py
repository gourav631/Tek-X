# Generated by Django 4.0 on 2022-09-03 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videou', '0002_video_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='name',
            field=models.CharField(blank=True, max_length=5000),
        ),
    ]
