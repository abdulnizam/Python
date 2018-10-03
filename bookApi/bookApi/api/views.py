from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

from api.models import Book

def index(request):

	results = json.dumps( [ { } ] )

	return HttpResponse(results, content_type='text/json' )

@csrf_exempt
def add_book(request):

	if request.method == 'POST':

		payload = json.loads( request.body )

		book = Book( name= payload['name'], value=payload['value'] )

		try:
			book.save()

			result = json.dumps([{'message' : 'success'}])

		except:
			result = json.dumps([{'message' : 'error'}])


	return HttpResponse( result, content_type='text/json')


def get_book(request, name):

	if request.method == 'GET':

		try:
			res = Book.objects.get(name=name)
			result = json.dumps([ { 'name' : res.name, 'value' : res.value } ])

		except:
			result = json.dumps([{'message' : 'no book found'}])

	return HttpResponse(result, content_type='text/json')