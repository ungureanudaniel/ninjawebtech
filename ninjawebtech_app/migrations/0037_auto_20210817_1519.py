# Generated by Django 3.1.9 on 2021-08-17 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ninjawebtech_app', '0036_auto_20210817_1516'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='active',
            new_name='approved',
        ),
    ]
