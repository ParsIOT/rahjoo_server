from __future__ import unicode_literals

from django.db import models


class Booth_Details(models.Model):
	name = models.CharField(max_length=100)
	owner = models.CharField(max_length=200)
	description = models.CharField(max_length=300)

	def __str__(self):
		return self.name
