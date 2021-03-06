# Generated by Django 3.1.9 on 2021-07-05 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ninjawebtech_app', '0027_delete_newsletteruser'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsletterUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=40)),
                ('conf_number', models.IntegerField()),
                ('confirmed', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
