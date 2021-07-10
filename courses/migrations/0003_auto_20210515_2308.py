# Generated by Django 3.0 on 2021-05-15 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20210515_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=200, primary_key=True, serialize=False, unique=True),
        ),
    ]
