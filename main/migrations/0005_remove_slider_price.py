# Generated by Django 5.1.5 on 2025-01-23 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_slider'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='price',
        ),
    ]
