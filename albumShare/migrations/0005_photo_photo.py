# Generated by Django 3.2.16 on 2023-01-12 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albumShare', '0004_auto_20230111_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
    ]
