# Generated by Django 4.0.6 on 2023-01-20 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0038_remove_orderdetail_order_total_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.order'),
        ),
    ]
