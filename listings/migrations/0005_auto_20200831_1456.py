# Generated by Django 3.1 on 2020-08-31 12:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20200831_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='listing_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 31, 14, 56, 44, 195236)),
        ),
    ]