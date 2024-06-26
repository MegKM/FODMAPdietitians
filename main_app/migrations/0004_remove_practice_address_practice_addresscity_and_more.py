# Generated by Django 4.2.4 on 2024-04-28 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_practice_latitiude_alter_practice_longitude'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practice',
            name='address',
        ),
        migrations.AddField(
            model_name='practice',
            name='addressCity',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='practice',
            name='addressCountry',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='practice',
            name='addressCounty',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='practice',
            name='addressPostCode',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='practice',
            name='addressState',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='practice',
            name='addressStreetNumberName',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
