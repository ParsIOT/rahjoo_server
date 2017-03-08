# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 12:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
	dependencies = [
		('boothManagement', '0004_product_details_owner_booth'),
	]

	operations = [
		migrations.AlterField(
			model_name='product_details',
			name='owner_booth',
			field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boothManagement.Booth_Details'),
		),
	]