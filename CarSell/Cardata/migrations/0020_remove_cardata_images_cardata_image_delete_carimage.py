# Generated by Django 4.1.7 on 2023-08-28 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cardata', '0019_carimage_remove_cardata_car_images_cardata_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardata',
            name='images',
        ),
        migrations.AddField(
            model_name='cardata',
            name='image',
            field=models.ImageField(default='', upload_to='CarImages/'),
        ),
        migrations.DeleteModel(
            name='Carimage',
        ),
    ]
