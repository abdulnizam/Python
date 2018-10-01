from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

from api.models import Car

def index(request):
	results = json.dumps([{}])
	return HttpResponse(results, content_type='text/json')

@csrf_exempt
def add_car(request):
	
	if request.method == 'POST':

		payload = json.loads(request.body)
		car_name = payload['car_name']
		value = payload['value']

		car = Car(name=car_name, value=value)

		try:
			car.save()
			results = json.dumps([{'message': 'Success' }])
		except:
			results = json.dumps([{'message': 'Error' }])

	
	return HttpResponse(results, content_type='text/json')


def get_car(request, car_name):

	if request.method == 'GET':

		try:
			res = Car.objects.get(name=car_name)
			results = json.dumps([{'car' : res.name, 'value': res.value}])
		except:
			results = json.dumps([{'message': 'Error' }])

	return HttpResponse(results, content_type='text/json')


