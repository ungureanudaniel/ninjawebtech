# Generated by Django 3.1.9 on 2021-07-03 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ninjawebtech_app', '0012_about_active'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Services',
            new_name='Service',
        ),
        migrations.RenameModel(
            old_name='Team',
            new_name='TeamMember',
        ),
    ]
