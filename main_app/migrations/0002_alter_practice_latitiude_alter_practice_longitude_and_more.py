# Generated by Django 4.2.4 on 2024-04-28 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practice',
            name='latitiude',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='practice',
            name='longitude',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='practice',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
