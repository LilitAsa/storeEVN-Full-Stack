# Generated by Django 5.1.5 on 2025-02-04 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['category'], 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
    ]
