# Generated by Django 2.1.7 on 2019-02-22 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_bed_heater_off_default_false'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_country_code',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]