# Generated by Django 4.1 on 2022-08-26 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("insight", "0013_alter_insightdata_opi"),
    ]

    operations = [
        migrations.RenameField(
            model_name="insightdata",
            old_name="initial_counter_reading",
            new_name="former_counter_reading",
        ),
        migrations.RenameField(
            model_name="insightdata",
            old_name="final_counter_reading",
            new_name="new_counter_reading",
        ),
    ]
