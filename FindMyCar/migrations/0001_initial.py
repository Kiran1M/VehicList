# Generated by Django 3.2.6 on 2021-08-15 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='zipInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.CharField(max_length=10)),
                ('state_code', models.CharField(max_length=5)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=50)),
            ],
        ),
    ]
