from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from geotour.models import Place
from geotour.models import Tour
from django.template.defaulttags import csrf_token
import datetime

from place_details_parser import *

def home(request):
	if request.method == 'POST':
		print request.POST['lat']
		destination = request.POST['destination']

		tour = Tour.objects.create(destination=destination) #save needed? TODO(jisha)
		tour.fromAddress = request.POST['fromAddress']
		tour.returnAddress = request.POST['returnAddress']
		fmt = '%m/%d/%Y %I:%M%p'
		d = datetime.datetime.strptime(request.POST['date']+" "+request.POST['startTime'], fmt)
		tour.startTime = d
		d = datetime.datetime.strptime(request.POST['date']+" "+request.POST['endTime'], fmt)
		# tour.startTime = request.POST['startTime']
		# tour.endTime = request.POST['endTime']
		tour.save()	
		#get_json_object_from_url(destination)
		tourId = tour.id
		# tourId = 1 #take this out
		return HttpResponseRedirect('/results/'+str(tourId))
	return render(request, 'home.html', {})


def update(request):
	return render(request, 'results.html', {})

def results(request, tourId):
	tour = Tour.objects.get(id = tourId)
	places = Place.objects.filter(tour = tour)
	searchResults = []
	tourPlaces = []
	return render(request, 'results.html', {'tourId': tourId,
		'searchResults': places, 'tourPlaces': places
		})

def change(request):
	tourId = request.POST['tourId']
	areas = request.POST.getlist('areas')

	searchResults = []
	tourPlaces = []

	tour = Tour.objects.get(id = tourId)
	places = []
	if areas != None and len(areas) != 0:
		areas_list = []
		for area in areas:
			try: 
				areas_list += [Area.objects.get(name = area)]
			except:
				pass
	return render_to_response('timeline.html', {'tourId': tourId, 'searchResults': searchResults, 'tourPlaces': tourPlaces},
	 context_instance=RequestContext(request))

def test(request):
	t = get_template('test.html')
	html = t.render(Context({}))
	return HttpResponse(html)
