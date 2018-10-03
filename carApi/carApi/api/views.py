# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from api.models import Car

from django.http import HttpResponse

import json
# Create your views here.

def index(request):
	results = json.dumps([{}]);

	return HttpResponse(results, content_type='text/json')

def add_data(request):

	if request.method == 'POST'

		payload = json.loads(request.body)

		car = Car(name=payload['name'], value=payload['value']);

		try:
			car.save()

			results = json.dumps([{'message' : 'success'}])

		except:
			results = json.dumps([{'message' : 'success'}])

	return HttpResponse(results, content_type='text/json')


def get_data(request, name):

	if request.method == 'GET'

		res = Car.objects.get(name=name)

		results = json.dumps
	