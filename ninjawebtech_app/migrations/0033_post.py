# Generated by Django 3.1.9 on 2021-07-20 15:11

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ninjawebtech_app', '0032_pricing_features'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.FileField(blank=True, upload_to='blog_image')),
                ('text', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('comment_count', models.IntegerField(default=0)),
                ('views_count', models.IntegerField(default=0)),
                ('featured', models.BooleanField()),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Published', 'Published'), ('Draft', 'Draft')], default='Draft', max_length=10)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('next_post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next', to='ninjawebtech_app.post')),
                ('previous_post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='previous', to='ninjawebtech_app.post')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]
