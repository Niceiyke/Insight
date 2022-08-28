# Generated by Django 4.1 on 2022-08-25 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insight', '0007_failuremode_function_failure'),
    ]

    operations = [
        migrations.AddField(
            model_name='deviation',
            name='details',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='insight.insightdata'),
        ),
        migrations.AddField(
            model_name='deviation',
            name='failure_mode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='insight.failuremode'),
        ),
        migrations.AddField(
            model_name='deviation',
            name='frequency',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deviation',
            name='function_failure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='insight.functionfailure'),
        ),
        migrations.AlterField(
            model_name='deviation',
            name='failure_mode_description',
            field=models.CharField(max_length=100),
        ),
    ]
