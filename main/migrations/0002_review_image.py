# Generated by Django 5.0.6 on 2024-06-03 19:16

import main.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=main.models.Review.user_directory_path),
        ),
    ]
