# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-13 10:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('boothManagement', '0005_advertisements_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisements_order',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]