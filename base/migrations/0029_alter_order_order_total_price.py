# Generated by Django 4.0.6 on 2022-12-24 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0028_rename_total_price_order_order_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_total_price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=100),
        ),
    ]
