# Generated by Django 4.1 on 2022-08-26 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("insight", "0016_alter_insightdata_opi"),
    ]

    operations = [
        migrations.AlterField(
            model_name="insightdata",
            name="opi",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=5, null=True
            ),
        ),
    ]