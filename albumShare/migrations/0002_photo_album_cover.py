# Generated by Django 3.2.16 on 2023-01-12 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albumShare', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='album_cover',
            field=models.BooleanField(default=False),
        ),
    ]