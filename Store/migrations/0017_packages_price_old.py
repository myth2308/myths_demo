# Generated by Django 5.0.4 on 2024-04-29 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0016_subscriber'),
    ]

    operations = [
        migrations.AddField(
            model_name='packages',
            name='price_old',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
