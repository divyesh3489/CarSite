# Generated by Django 4.2.4 on 2023-08-21 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cardata', '0004_rename_caride_cardata_caride_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardata',
            name='carbrand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Cardata.carbrand'),
        ),
        migrations.AlterField(
            model_name='cardata',
            name='carmodel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Cardata.carmodel'),
        ),
    ]