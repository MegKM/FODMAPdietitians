# Generated by Django 4.2.4 on 2024-04-28 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_practice_address_practice_addresscity_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='practice',
            old_name='addressCounty',
            new_name='addressSuburb',
        ),
    ]
