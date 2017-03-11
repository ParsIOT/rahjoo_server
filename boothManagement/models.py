from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Booth_Owner_Profile(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	company = models.CharField(max_length=50)
	phone = models.CharField(max_length=12)
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
	owner_booth = models.ForeignKey(Booth_Owner_Profile, on_delete=models.CASCADE)

	def __str__(self):
		return self.name + " owned by " + self.owner_booth.name
