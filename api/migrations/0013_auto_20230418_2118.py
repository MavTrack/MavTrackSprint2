# Generated by Django 3.2 on 2023-04-19 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20230418_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingschedule',
            name='friday_distance',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trainingschedule',
            name='monday_distance',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trainingschedule',
            name='saturday_distance',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trainingschedule',
            name='sunday_distance',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trainingschedule',
            name='thursday_distance',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trainingschedule',
            name='tuesday_distance',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trainingschedule',
            name='wednesday_distance',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
