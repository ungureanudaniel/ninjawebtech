# Generated by Django 3.1.9 on 2021-10-04 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ninjawebtech_app', '0042_auto_20210914_2226'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostViews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IPAddress', models.GenericIPAddressField(default='45.243.82.169')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ninjawebtech_app.post')),
            ],
        ),
    ]
