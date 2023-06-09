# Generated by Django 4.1.7 on 2023-04-26 03:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_order_address_order_mobile_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 4, 26, 9, 11, 16, 455060)),
        ),
        migrations.AlterField(
            model_name='order',
            name='mobile',
            field=models.CharField(blank=True, default='', max_length=12),
        ),
    ]
