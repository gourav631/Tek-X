# Generated by Django 4.0 on 2022-09-04 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videou', '0004_remove_video_name_video_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='summary',
            field=models.CharField(max_length=5000, null=True),
        ),
    ]
