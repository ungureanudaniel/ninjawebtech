# Generated by Django 3.1.9 on 2021-08-17 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ninjawebtech_app', '0035_delete_contactdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
