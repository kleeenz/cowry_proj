# Generated by Django 3.1.7 on 2021-05-24 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cowry', '0004_auto_20210523_1940'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unique_field',
            old_name='timeStampFfield',
            new_name='timeStampField',
        ),
    ]
