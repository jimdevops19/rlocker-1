# Generated by Django 3.2 on 2022-08-01 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=64, unique=True)),
                ('application_name', models.CharField(max_length=64, unique=True)),
                ('package_url', models.CharField(blank=True, default=None, max_length=512, null=True, unique=True)),
                ('project_url', models.CharField(blank=True, default=None, max_length=512, null=True, unique=True)),
                ('is_installed', models.BooleanField(default=False)),
            ],
        ),
    ]
