# Generated by Django 3.2.13 on 2022-06-05 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ninjawebtech_app', '0055_alter_post_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='link',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
    ]