# Generated by Django 3.2.6 on 2021-08-15 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FindMyCar', '0008_remove_vehicle_listings_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle_listings',
            name='amenities',
            field=models.TextField(null=True),
        ),
    ]
