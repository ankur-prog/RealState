# Generated by Django 3.1 on 2020-08-30 20:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='listing_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 30, 22, 20, 48, 348508)),
        ),
    ]