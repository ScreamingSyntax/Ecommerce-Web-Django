# Generated by Django 4.2.2 on 2023-07-09 06:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 7, 9, 6, 53, 33, 190940, tzinfo=datetime.timezone.utc)),
        ),
    ]
