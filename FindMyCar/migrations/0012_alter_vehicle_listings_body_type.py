# Generated by Django 3.2.6 on 2021-08-15 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FindMyCar', '0011_alter_vehicle_listings_distance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle_listings',
            name='body_type',
            field=models.CharField(max_length=50),
        ),
    ]