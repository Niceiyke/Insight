# Generated by Django 4.1 on 2022-08-31 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insight', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deviation',
            name='status',
            field=models.CharField(choices=[('Resolved', 'Resolved'), ('Pending', 'Pending'), ('Fixed', 'Fixed')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]
