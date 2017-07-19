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
	image = models.FileField(upload_to='images/%Y/%m/%d', max_length=255, blank=True, null=True, default='default/profile-big.png')

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
	image = models.FileField(upload_to='images/%Y/%m/%d', max_length=255, blank=True, null=True, default='default/mptr2-01.jpg')

	def __str__(self):
		return "Product '" + self.name + "' owned by booth '" + self.owner_booth.boothName + "'"


class Advertisement_Area(models.Model):
	section_name = models.CharField(max_length=30)
	topLeft_x = models.DecimalField(max_digits=5, decimal_places=2)
	topLeft_y = models.DecimalField(max_digits=5, decimal_places=2)
	bottomRight_x = models.DecimalField(max_digits=5, decimal_places=2)
	bottomRight_y = models.DecimalField(max_digits=5, decimal_places=2)
	base_price = models.IntegerField()

	def __str__(self):
		return self.section_name


class Advertisements_order(models.Model):
	id = models.AutoField(primary_key=True)
	advertisement_areas = models.ManyToManyField(Advertisement_Area)
	owner_booth = models.ForeignKey(Booth_Owner, on_delete=models.CASCADE)
	totalPrice = models.IntegerField()
	discount = models.IntegerField(default=0)
	advertisement_name = models.CharField(max_length=30, default='')
	advertisement_text = models.CharField(max_length=200, default='')

	def __str__(self):
		return self.advertisement_name

# def _calc_totalCost(self):
# 	t_cost = 0
# 	for advArea in self.advertisement_areas:
# 		t_cost += advArea.base_price
# 	t_cost -= self.discount
# 	return t_cost

# total_price = property(_calc_totalCost)
