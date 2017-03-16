from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Booth_Owner(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	boothName = models.CharField(max_length=50)
	company = models.CharField(max_length=50)
	phone = models.CharField(max_length=12)
	description = models.CharField(max_length=300)

	def __str__(self):
		# return  str("Booth '" + str(self.boothName) + "' owned by '" + str(self.user.username) + "'")
		return self.boothName


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Booth_Owner.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
# 	instance.BoothOwner.save()


class Product_Details(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	model = models.CharField(max_length=100)
	description = models.CharField(max_length=300)
	price = models.IntegerField()
	status = models.BooleanField(default=True)
	owner_booth = models.ForeignKey(Booth_Owner, on_delete=models.CASCADE)

	def __str__(self):
		return "Product '" + self.name + "' owned by booth '" + self.owner_booth.boothName + "'"
