from django.contrib import admin
from .models import *


class ProductDetailsAdmin(admin.ModelAdmin):
	# fields = ['owner', 'name']
	list_display = ('id', 'name', 'price', 'status', 'owner_booth')
	list_filter = ['status', 'owner_booth']
	search_fields = ['name', 'price', 'description', 'model']


# Register your models here.
admin.site.register(Product_Details, ProductDetailsAdmin)
admin.site.register(Booth_Owner)
admin.site.register(Advertisement_Area)
admin.site.register(Advertisements_order)
