import http
import simplejson as json
from django.template import RequestContext
from django.utils.translation import ugettext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login, logout
from .forms import Booth_Owner_Profile
from .models import *


def change_language(request, template_name):
    if request.LANGUAGE_CODE == 'fa':
        html = template_name.split('.')[0] + '-fa.html'
    else:
        html = template_name
    return html


def index(request):
    template = loader.get_template('set_language.html')
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
    html = change_language(request, 'Booth_Management.html')
    return render_to_response(html, RequestContext(request, {'form': profile_form}))


# @login_required
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


# @login_required
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
    html = change_language(request, 'Products_Details.html')
    return render_to_response(html, {'response': response})


# @login_required
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


# @login_required(login_url='/booth/login')
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


def advertisement(request):
    response = []
    allAdvertisementAreas = Advertisement_Area.objects.all()
    for area in allAdvertisementAreas:
        response.append({'section_name': area.section_name, 't_x': area.topLeft_x, 't_y': area.topLeft_y, 'b_x': area.bottomRight_x, 'b_y': area.bottomRight_y, 'base_price': area.base_price})
    html = change_language(request, 'Advertisements.html')
    return render_to_response(html, {'response': json.dumps(response)})


def checkServer(request):
    return HttpResponse(json.dumps({'status': 'ok'}), content_type="application/json")


def user_logout(request):
    logout(request)


def advertisementJson(request):
    response = {}
    try:
        allAdvertisementOrders = Advertisements_order.objects.all()
        for order in allAdvertisementOrders:
            areaRes = []
            for advArea in order.advertisement_areas.all():
                areaRes.append({'section_name': advArea.section_name, 't_x': advArea.topLeft_x, 't_y': advArea.topLeft_y, 'b_x': advArea.bottomRight_x, 'b_y': advArea.bottomRight_y})
            response = {'status': 'OK', 'id': order.id, 'sections': areaRes, 'name': order.advertisement_name, 'text': order.advertisement_text}
    except:
        response = {'status': 'Error'}
    return HttpResponse(json.dumps(response), content_type="application/json")
