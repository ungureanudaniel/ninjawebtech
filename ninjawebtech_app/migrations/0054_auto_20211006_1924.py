# Generated by Django 3.1.9 on 2021-10-06 19:24

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('ninjawebtech_app', '0053_auto_20211006_1912'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogTags',
            new_name='BlogTag',
        ),
    ]
