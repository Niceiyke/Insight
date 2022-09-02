# Generated by Django 4.1 on 2022-09-02 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insight', '0003_alter_equipment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='name',
            field=models.CharField(choices=[('Filler', 'Filler'), ('Bottle washer', 'Bottle washer'), ('Labeller', 'Labeller'), ('EBI', 'EBI'), ('Packer', 'Packer'), ('Unpacker', 'Unpacker'), ('Palletizer', 'Palletizer'), ('Depalletizer', 'Depalletizer'), ('Crate Conveyor', 'Crate Conveyor'), ('BConv-unpacker-Bwasher', 'BConv-unpacker-Bwasher'), ('BConv-Bwasher-fill', 'BConv-Bwasher-filler'), ('BConv-filler-labeller', 'BConv-filler-labeller'), ('BConv-labeller-packer', 'BConv-labeller-packer')], max_length=100),
        ),
    ]