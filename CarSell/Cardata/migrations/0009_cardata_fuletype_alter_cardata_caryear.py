# Generated by Django 4.1.7 on 2023-08-22 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cardata', '0008_cardata_caryear_alter_cardata_caride'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardata',
            name='fuletype',
            field=models.CharField(choices=[('CNG', 'CNG'), ('Petrol', 'Petrol'), ('Diesel', 'Diesel')], default='Petrol', max_length=6),
        ),
        migrations.AlterField(
            model_name='cardata',
            name='caryear',
            field=models.IntegerField(choices=[('', ''), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023)], default=2023),
        ),
    ]
