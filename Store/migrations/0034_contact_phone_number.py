# Generated by Django 5.0.4 on 2024-05-05 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0033_remove_contact_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(default='', max_length=15),
        ),
    ]
