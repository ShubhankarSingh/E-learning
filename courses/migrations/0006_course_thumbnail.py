# Generated by Django 3.0 on 2021-05-30 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20210530_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='thumbnails/'),
        ),
    ]
