# Generated by Django 4.1 on 2022-08-24 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insight', '0005_alter_equipment_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='failure_mode',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='function_failure',
        ),
        migrations.CreateModel(
            name='FunctionFailure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insight.equipment')),
            ],
        ),
        migrations.CreateModel(
            name='FailureMode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insight.equipment')),
            ],
        ),
    ]
