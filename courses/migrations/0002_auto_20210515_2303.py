# Generated by Django 3.0 on 2021-05-15 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('slug', models.SlugField(default='', max_length=200, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='id',
        ),
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='language',
            field=models.CharField(default='English', max_length=200),
        ),
        migrations.AddField(
            model_name='course',
            name='short_description',
            field=models.TextField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(default='', max_length=200, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.Category'),
        ),
    ]
