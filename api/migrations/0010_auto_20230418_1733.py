# Generated by Django 3.2 on 2023-04-18 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20230418_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='PromptsEncouragement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prompt', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='trainingplan',
            name='train_cat',
        ),
        migrations.RemoveField(
            model_name='trainingplan',
            name='train_goal',
        ),
        migrations.RemoveField(
            model_name='trainingplan',
            name='weekly_skd',
        ),
        migrations.RemoveField(
            model_name='trainingpreference',
            name='rest_day',
        ),
        migrations.RemoveField(
            model_name='trainingpreference',
            name='train_plan',
        ),
        migrations.RemoveField(
            model_name='trainingschedule',
            name='daily_task',
        ),
        migrations.DeleteModel(
            name='DailyTasks',
        ),
        migrations.DeleteModel(
            name='TrainingPlan',
        ),
    ]
