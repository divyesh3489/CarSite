# Generated by Django 4.2.4 on 2023-08-23 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cardata', '0014_cardata_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardata',
            name='car_images',
            field=models.ImageField(default='', upload_to='CarImages'),
        ),
    ]