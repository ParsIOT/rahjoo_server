import http, json
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.shortcuts import render
from .forms import Booth_Details_Form

from .models import Booth_Details


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


def view_booth_details(request):
	booths = Booth_Details.objects.all()
	response = {}
	r = {}
	for booth in booths:
		r['name'] = booth.name
		r['owner'] = booth.owner
		r['description'] = booth.description
		response[booth.id] = r
		r = {}
	# return JsonResponse(serializers.serialize('json', booths), safe=False)
	return HttpResponse(json.dumps(response), content_type="application/json")
