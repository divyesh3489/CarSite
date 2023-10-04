# Generated by Django 4.1.7 on 2023-10-04 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cardata', '0005_alter_carmodel_boot_space_alter_carmodel_doors_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='cardata',
            name='city',
            field=models.CharField(default='', max_length=50),
        ),
    ]
