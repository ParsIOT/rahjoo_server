# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-17 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
	dependencies = [
		('boothManagement', '0001_initial'),
	]

	operations = [
		migrations.AddField(
			model_name='booth_owner',
			name='image',
			field=models.FileField(blank=True, max_length=255, null=True, upload_to='images/%Y/%m/%d'),
		),
	]
