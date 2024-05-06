# Generated by Django 5.0.4 on 2024-05-01 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0025_delete_carousel_remove_booking_booking_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='carousel_img/')),
            ],
        ),
        migrations.RenameField(
            model_name='subscriber',
            old_name='subscribed_at',
            new_name='subscriber_at',
        ),
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
        migrations.AlterField(
            model_name='destination',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
