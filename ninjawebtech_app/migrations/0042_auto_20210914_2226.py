# Generated by Django 3.1.9 on 2021-09-14 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ninjawebtech_app', '0041_post_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pricingfeatures',
            old_name='feature',
            new_name='feature_de',
        ),
        migrations.AddField(
            model_name='pricingfeatures',
            name='feature_en',
            field=models.CharField(default='a', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pricingfeatures',
            name='feature_ro',
            field=models.CharField(default='a', max_length=30),
            preserve_default=False,
        ),
    ]