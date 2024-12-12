# Generated by Django 5.1.2 on 2024-10-28 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sko_Adminside', '0016_brand'),
    ]

    operations = [
        migrations.DeleteModel(
            name='brand',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AlterUniqueTogether(
            name='variants',
            unique_together=set(),
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
        migrations.RemoveField(
            model_name='variants',
            name='product',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
