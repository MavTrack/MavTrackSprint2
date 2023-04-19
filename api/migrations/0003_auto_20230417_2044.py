# Generated by Django 3.2 on 2023-04-18 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20230417_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainingschedule',
            name='daily_task',
        ),
        migrations.AddField(
            model_name='trainingschedule',
            name='daily_task',
            field=models.ManyToManyField(blank=True, to='api.DailyTask'),
        ),
    ]
