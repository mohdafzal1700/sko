# Generated by Django 5.1.2 on 2024-11-22 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sko_Adminside', '0052_coupon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='Offer_type',
        ),
    ]
