from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.db.models import Sum

from boothManagement import models
import json


def editProductDetails(request):
	if request.is_ajax():
		try:
			response = {}
			username = request.user.username
			productName = request.GET.get('productName', None)
			productModel = request.GET.get('productModel', None)
			productPrice = request.GET.get('productPrice', None)
			productStatus = json.loads(request.GET.get('productStatus', 'false'))
			productDescription = request.GET.get('productDescription', None)
			if checkProductOwner(username, productName):
				product = models.Product_Details.objects.get(name=productName)
				product.model = productModel
				product.price = productPrice
				product.status = productStatus
				product.description = productDescription
				product.save()
				response['status'] = True
				response['n_model'] = productModel
				response['n_price'] = productPrice
				response['n_status'] = productStatus
				response['n_description'] = productDescription
		except:
			response = {'status': False}
		return HttpResponse(json.dumps(response), content_type='application.json')
	return HttpResponseForbidden()


def checkProductOwner(username, productName):
	currentBoothOwner = models.Booth_Owner.objects.get(user__username=username)
	ownerAllProducts = models.Product_Details.objects.filter(owner_booth=currentBoothOwner).values_list('name', flat=True)
	if productName in ownerAllProducts:
		return True
	else:
		return False


def makeAdvertisementsOrder(request):
	if request.is_ajax():
		try:
			response = {}
			advertisement_name = request.GET.get('advertisement_name', None)
			advertisement_text = request.GET.get('advertisement_text', None)
			selectedSections = models.Advertisement_Area.objects.filter(section_name__in=request.GET.getlist('selectedSections[]'))
			total_price = selectedSections.aggregate(Sum('base_price'))
			advertisement_order = models.Advertisements_order.objects.create(advertisement_name=advertisement_name, advertisement_text=advertisement_text, totalPrice=total_price['base_price__sum'])
			advertisement_order.save()
			advertisement_order.advertisement_areas.add(*(selectedSections))
			# advertisement_order.advertisement_areas.add(models.Advertisement_Area.objects.all()[2])
			advertisement_order.save()
		except:
			response = {'status': False}
		return HttpResponse(json.dumps(response), content_type='application.json')
	return HttpResponseForbidden()