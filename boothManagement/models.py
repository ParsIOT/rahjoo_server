from __future__ import unicode_literals

from django.db import models


class Booth_Details(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	owner = models.CharField(max_length=200)
	description = models.CharField(max_length=300)

	def __str__(self):
		return self.name


class Product_Details(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	model = models.CharField(max_length=100)
	description = models.CharField(max_length=300)
	price = models.IntegerField()
	status = models.BooleanField(default=True)
