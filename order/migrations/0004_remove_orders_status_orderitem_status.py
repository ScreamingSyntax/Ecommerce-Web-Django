# Generated by Django 4.2.2 on 2023-07-11 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_remove_orders_products_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='status',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('Order Recieved', 'Order Recieved'), ('Order Processing', 'Order Processing'), ('On The Way', 'On the Way'), ('Order completed', 'Order completed')], default='Order Recieved', max_length=250, null=True),
        ),
    ]
