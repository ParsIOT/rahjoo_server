from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.db.models import Sum

from boothManagement import models
from boothManagement.models import Product_Details
import json


def editProductDetails(request):
    if request.is_ajax():
        try:
            response = {}
            username = request.user.username
            productID = request.GET.get('productID', None)
            productName = request.GET.get('productName', None)
            productModel = request.GET.get('productModel', None)
            productPrice = request.GET.get('productPrice', None)
            productStatus = json.loads(request.GET.get('productStatus', 'false'))
            productDescription = request.GET.get('productDescription', None)
            if checkProductOwner(username, productID):
                product = models.Product_Details.objects.get(id=productID)
                product.name = productName
                product.model = productModel
                product.price = productPrice
                product.status = productStatus
                product.description = productDescription
                product.save()
                response['status'] = True
                response['n_name'] = productName
                response['n_model'] = productModel
                response['n_price'] = productPrice
                response['n_status'] = productStatus
                response['n_description'] = productDescription
        except:
            response = {'status': False}
        return HttpResponse(json.dumps(response), content_type='application.json')
    return HttpResponseForbidden()


def newProductDetails(request):
    if request.is_ajax():
        try:
            response = {}
            bootOwner = models.Booth_Owner.objects.get(user=request.user)
            productName = request.GET.get('productName', None)
            productModel = request.GET.get('productModel', None)
            productPrice = request.GET.get('productPrice', None)
            productStatus = json.loads(request.GET.get('productStatus', 'false'))
            productDescription = request.GET.get('productDescription', None)

            product = models.Product_Details.objects.create(name=productName, model=productModel, description=productDescription, price=productPrice, status=productStatus, owner_booth=bootOwner)
            product.save()
            response['status'] = True
            response['n_name'] = productName
            response['n_model'] = productModel
            response['n_price'] = productPrice
            response['n_status'] = productStatus
            response['n_description'] = productDescription
        except:
            response = {'status': False}
        return HttpResponse(json.dumps(response), content_type='application.json')
    return HttpResponseForbidden()


def checkProductOwner(username, productID):
    currentBoothOwner = models.Booth_Owner.objects.get(user__username=username)
    ownerAllProducts = models.Product_Details.objects.filter(owner_booth=currentBoothOwner).values_list('id', flat=True)
    if int(productID) in ownerAllProducts:
        return True
    else:
        return False


def makeAdvertisementsOrder(request):
    if request.is_ajax():
        try:
            response = {}
            advertisement_name = request.GET.get('advertisement_name', None)
            advertisement_text = request.GET.get('advertisement_text', None)
            advertisement_id = request.GET.get('advertisement_id', None)
            add_or_edit = request.GET.get('add_or_edit')
            currentBoothOwner = models.Booth_Owner.objects.get(user=request.user)
            advertisement_selectedSections = models.Advertisement_Area.objects.filter(section_name__in=request.GET.getlist('selected_sections[]')[0].split(','))
            total_price = list(advertisement_selectedSections.aggregate(Sum('base_price')).values())[0]


            # if the request is adding a new order
            if(add_or_edit=='add'):
                advertisement_order = models.Advertisements_order.objects.create(advertisement_name=advertisement_name, advertisement_text=advertisement_text, totalPrice=total_price['base_price__sum'], owner_booth=currentBoothOwner)
            elif(add_or_edit=='edit'):
                modifiedAdvertisement = models.Advertisements_order.objects.get(id=advertisement_id)
                # check if the owner and the modified adv user are same or not
                if(modifiedAdvertisement.owner_booth.user == currentBoothOwner.user):
                    modifiedAdvertisement.advertisement_name = advertisement_name
                    modifiedAdvertisement.advertisement_text = advertisement_text
                    modifiedAdvertisement.advertisement_areas = advertisement_selectedSections
                    modifiedAdvertisement.totalPrice = total_price
                    modifiedAdvertisement.save()
                    response['status'] = True
                    response['n_advertisement_name'] = advertisement_name
                    response['n_advertisement_text'] = advertisement_text
                    response['n_total_price'] = total_price
            else:
                HttpResponseForbidden()
            # advertisement_order.save()
            # advertisement_order.advertisement_areas.add(*(advertisement_selectedSections))
            # advertisement_order.advertisement_areas.add(models.Advertisement_Area.objects.all()[2])
            # advertisement_order.save()
        except:
            response = {'status': False}
        return HttpResponse(json.dumps(response), content_type='application.json')
    return HttpResponseForbidden()


def getAdvertisementsAreas(request):
    if request.is_ajax():
        try:
            response = {'status': True, 'init_selected_sections': [], 'init_price': 0}
            advertisement_name = request.GET.get('adv_name', None)
            advertisement_text = request.GET.get('adv_text', None)
            adv_order = models.Advertisements_order.objects.get(advertisement_name=advertisement_name, advertisement_text=advertisement_text)
            selected_sections = adv_order.advertisement_areas.all()
            init_price = 0
            for area in selected_sections:
                response['init_selected_sections'].append(area.section_name)
                init_price += area.base_price
            response['init_price'] = init_price
        except:
            response = {'status': False}
        return HttpResponse(json.dumps(response), content_type='application.json')
    return HttpResponseForbidden()
