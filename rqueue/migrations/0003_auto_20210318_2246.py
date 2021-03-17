# Generated by Django 3.1.2 on 2021-03-18 20:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rqueue', '0002_auto_20210318_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rqueue',
            name='priority',
            field=models.IntegerField(default=3, validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(3)]),
        ),
    ]
