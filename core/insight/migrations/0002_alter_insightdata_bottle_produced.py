# Generated by Django 4.1 on 2022-08-24 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insight', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insightdata',
            name='bottle_produced',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]