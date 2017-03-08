import http, json
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.shortcuts import render, render_to_response
from .forms import Booth_Details_Form

from .models import Booth_Details, Product_Details


def index(request):
	template = loader.get_template('Booth_Management.html')
	context = {}
	return HttpResponse(template.render(context, request))


def save_booth_details(request):
	if request.method == 'POST':
		form = Booth_Details_Form(data=request.POST)
		print(form.errors)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('#')
	else:
		form = Booth_Details_Form()

	return render(request, 'Booth_Management.html', {'form': form})


def view_booth_List(request):
	booths = Booth_Details.objects.all()
	response = {'booths': []}
	r = {}
	for booth in booths:
		r['name'] = booth.name
		r['owner'] = booth.owner
		r['description'] = booth.description
		response['booths'].append(r)
		r = {}
	return HttpResponse(json.dumps(response), content_type="application/json")


def view_products_details(request):
	response = {}
	all_products = Product_Details.objects.all()
	d = {}
	for product in all_products:
		d['name'] = product.name
		d['model'] = product.model
		d['description'] = product.description
		d['price'] = product.price
		d['status'] = product.status
		response[product.id] = d
		d = {}
	return render_to_response('Products_Details.html', {'response': response})


def view_Products_list(request):
	response = {'products_list': []}
	all_products = Product_Details.objects.order_by('name')
	d = {}
	for product in all_products:
		d['name'] = product.name
		d['model'] = product.model
		d['description'] = product.description
		d['price'] = product.price
		d['status'] = product.status
		d['owner_booth'] = product.owner_booth.id
		response['products_list'].append(d)
		d = {}
	return HttpResponse(json.dumps(response), content_type="application/json")


def view_booth_products(request, booth_Id):
	boothProducts = Product_Details.objects.filter(owner_booth__id=booth_Id)
	response = {'booth_Products': []}
	d = {}
	for product in boothProducts:
		d['name'] = product.name
		d['model'] = product.model
		d['description'] = product.description
		d['price'] = product.price
		d['status'] = product.status
		d['owner_booth'] = product.owner_booth.id
		response['booth_Products'].append(d)
		d = {}
	return HttpResponse(json.dumps(response), content_type="application/json")
