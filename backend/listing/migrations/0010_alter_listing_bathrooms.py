# Generated by Django 4.2.3 on 2023-08-04 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0009_alter_listing_home_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bathrooms',
            field=models.IntegerField(),
        ),
    ]
