# Generated by Django 5.0.3 on 2024-03-11 15:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=6)),
                ('nationality', models.CharField(max_length=40)),
                ('author_image', models.URLField(blank=True, null=True)),
                ('year_born', models.PositiveIntegerField(default=1800, validators=[django.core.validators.MinValueValidator(1800)])),
                ('year_died', models.PositiveIntegerField(blank=True, null=True)),
                ('biography', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
