# Generated by Django 3.1.9 on 2021-07-20 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ninjawebtech_app', '0029_auto_20210705_1910'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=10)),
                ('highlighted', models.BooleanField(default=False)),
            ],
        ),
    ]
