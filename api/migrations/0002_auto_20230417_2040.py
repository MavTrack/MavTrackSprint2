# Generated by Django 3.2 on 2023-04-18 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainingschedule',
            name='daily_task',
        ),
        migrations.AddField(
            model_name='trainingschedule',
            name='daily_task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.dailytask'),
        ),
    ]
