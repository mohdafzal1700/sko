# Generated by Django 5.1.2 on 2024-11-24 15:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sko_Adminside', '0060_remove_order_cart_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Sko_Adminside.cart'),
        ),
    ]