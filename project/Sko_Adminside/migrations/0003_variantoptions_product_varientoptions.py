# Generated by Django 5.1.2 on 2024-10-24 10:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sko_Adminside', '0002_remove_product_varientoptions_productimage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VariantOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_name', models.CharField(max_length=255)),
                ('option_value', models.CharField(max_length=255)),
                ('is_delete', models.BooleanField(default=False)),
                ('variants', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='Sko_Adminside.variants')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='varientoptions',
            field=models.ManyToManyField(related_name='products_variant_options', to='Sko_Adminside.variantoptions'),
        ),
    ]
