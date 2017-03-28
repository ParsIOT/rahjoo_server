import http
import simplejson as json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login, logout
from .forms import Booth_Owner_Profile, Login_Form
from .models import *


def index(request):
	template = loader.get_template('Booth_Management.html')
	context = {}
	return HttpResponse(template.render(context, request))


@login_required
def BoothOwnerProfile(request):
	currentUser = Booth_Owner.objects.get(user=request.user)
	profile_form = Booth_Owner_Profile(data=request.POST or None, user=request.user, request=request)
	if request.method == 'POST':
		if profile_form.is_valid():
			profile_form.instance = Booth_Owner.objects.get(user=request.user)
			profile_form.save(commit=False)
			profile_form.user = request.user
			profile_form.save()
			return HttpResponseRedirect('#')
	else:
		init_data = {'firstName': currentUser.user.first_name, 'lastName': currentUser.user.last_name,
		             'email': currentUser.user.email, 'company': currentUser.company,
		             'boothName': currentUser.boothName, 'phone': currentUser.phone,
		             'description': currentUser.description}
		profile_form.initial = init_data

	return render(request, 'Booth_Management.html', {'form': profile_form})


@login_required
def view_booth_List(request):
	booths = Booth_Owner_Profile.objects.all()
	response = {'booths': []}
	r = {}
	for booth in booths:
		r['name'] = booth.BoothName
		r['owner'] = booth.owner.user.get_username()
		r['description'] = booth.description
		response['booths'].append(r)
		r = {}
	return HttpResponse(json.dumps(response), content_type="application/json")


@login_required
def view_products_details(request):
	currentUser = User.objects.get(username=request.user.username)
	response = {}
	user_all_products = Product_Details.objects.filter(owner_booth__user=currentUser)
	d = {}
	for product in user_all_products:
		d['name'] = product.name
		d['model'] = product.model
		d['description'] = product.description
		d['price'] = product.price
		d['status'] = product.status
		response[product.id] = d
		d = {}
	return render_to_response('Products_Details.html', {'response': response})


@login_required
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
		d['owner_booth_id'] = product.owner_booth.id
		response['products_list'].append(d)
		d = {}
	return HttpResponse(json.dumps(response), content_type="application/json")


@login_required(login_url='/booth/login')
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
		response['booth_Products'].append(d)
		d = {}
	return HttpResponse(json.dumps(response), content_type="application/json")


def user_login(request):
	if request.method == 'POST':
		login_form = Login_Form(data=request.POST)
		if login_form.is_valid():
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect('/booth/saveBoothDetails')
			else:
				pass
	else:
		login_form = Login_Form()
	return render(request, 'login.html', {'login_form': login_form})


def advertisement(request):
	response = []
	allAdvertisementAreas = Advertisement_Area.objects.all()
	for area in allAdvertisementAreas:
		response.append({'section_name': area.section_name, 't_x': area.topLeft_x, 't_y': area.topLeft_y, 'b_x': area.bottomRight_x, 'b_y': area.bottomRight_y, 'base_price': area.base_price})

	return render(request, 'Advertisements.html', {'response': json.dumps(response)})
