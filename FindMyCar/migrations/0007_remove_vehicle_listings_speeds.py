# Generated by Django 3.2.6 on 2021-08-15 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FindMyCar', '0006_auto_20210816_0238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle_listings',
            name='speeds',
        ),
    ]
