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
	response = {}
	r = {}
	for booth in booths:
		r['name'] = booth.name
		r['owner'] = booth.owner
		r['description'] = booth.description
		response[booth.id] = r
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
