# Generated by Django 5.0.3 on 2024-03-11 17:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpostcomment',
            name='to_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blogpost'),
        ),
    ]
