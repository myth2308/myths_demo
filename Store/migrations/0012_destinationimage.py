# Generated by Django 5.0.4 on 2024-04-23 20:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0011_remove_destination_name_delete_destinationimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='DestinationImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='destination_images/')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Store.destination')),
            ],
        ),
    ]
