# Generated by Django 3.2.6 on 2021-08-15 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FindMyCar', '0005_alter_vehicle_listings_trim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle_listings',
            name='exterior',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='vehicle_listings',
            name='trim',
            field=models.CharField(max_length=80),
        ),
    ]
