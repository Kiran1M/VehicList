# Generated by Django 3.2.6 on 2021-08-16 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FindMyCar', '0018_auto_20210816_0332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealers',
            name='dealer_number',
            field=models.CharField(max_length=20),
        ),
    ]
