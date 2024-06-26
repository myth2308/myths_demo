# Generated by Django 5.0.4 on 2024-04-30 17:48

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0019_alter_destinationimage_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='carousel_img/')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('destination_name', models.CharField(max_length=100)),
            ],
        ),
    ]
