# Generated by Django 3.2.6 on 2021-08-15 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FindMyCar', '0013_alter_vehicle_listings_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle_listings',
            name='transmission',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
