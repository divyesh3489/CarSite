# Generated by Django 4.1.7 on 2023-08-28 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cardata', '0021_alter_cardata_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardata',
            name='image',
        ),
        migrations.CreateModel(
            name='CarImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='car_images/')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cardata.cardata')),
            ],
        ),
    ]
