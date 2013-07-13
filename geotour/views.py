
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from geotour.models import Place
from geotour.models import Tour
from django.template.defaulttags import csrf_token

from place_details_parser import *

def home(request, lat, lng):
	if request.method == 'POST':
		destination = request.POST['destination']
		tour = Tour.objects.create(destination=destination) #save needed? TODO(jisha)
		tour.fromAddress = request.POST['fromAddress']
		tour.returnAddress = request.POST['returnAddress']
		tour.startTime = request.POST['startTime']
		tour.endTime = request.POST['endTime']
		tour.lat = request.POST['lat']
		tour.lng = request.POST['lng']
		tour.save()	
		# tourId = tour.id
		tourId = 1 #take this out
		return HttpResponseRedirect('/results/'+str(tourId))
	return render(request, 'home.html', {})

def results(request, tourId):
	tour = Tour.objects.get(id = tourId)
	places = Place.objects.filter(tour = tour)

	return render(request, 'results.html', {
		'places': places
		})

def filter(request):
	tourId = request.POST['tourId']
	areas = request.POST.getlist('areas')
	places = []
	tour = Tour.objects.get(id = tourId)
	if areas != None and len(areas) != 0:
		areas_list = []
		for area in areas:
			try: 
				areas_list += [Area.objects.get(name = area)]
			except:
				pass
	#add areas to database?
	return render_to_response('timeline.html', places, context_instance=RequestContext(request))

def test(request):
	t = get_template('test.html')
	html = t.render(Context({}))
	return HttpResponse(html)
