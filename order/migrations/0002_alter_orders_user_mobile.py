# Generated by Django 4.2.2 on 2023-07-11 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='user_mobile',
            field=models.IntegerField(),
        ),
    ]
