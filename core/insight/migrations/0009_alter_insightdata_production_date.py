# Generated by Django 4.1 on 2022-08-25 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insight', '0008_deviation_details_deviation_failure_mode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insightdata',
            name='production_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
