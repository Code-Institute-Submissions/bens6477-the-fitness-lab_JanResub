# Generated by Django 3.2 on 2023-01-19 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='brand',
            new_name='brand_name',
        ),
    ]
