# Generated by Django 5.0.4 on 2024-05-01 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0023_carousel_alter_destination_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='contact_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
