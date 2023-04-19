# Generated by Django 3.2 on 2023-04-18 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20230418_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainingschedule',
            name='train_pref',
        ),
        migrations.AddField(
            model_name='trainingschedule',
            name='train_pref',
            field=models.ManyToManyField(blank=True, to='api.TrainingPreference'),
        ),
    ]
