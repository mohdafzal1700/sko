# Generated by Django 5.1.2 on 2024-11-20 14:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sko_Adminside', '0041_alter_wishlist_varients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='varients',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlists', to='Sko_Adminside.variants'),
        ),
    ]
