
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from geotour.models import Place
from geotour.models import Tour
from django.template.defaulttags import csrf_token

include place_details_parser.py

def home(request):
	if request.method == 'POST':
		destination = request.POST['destination']
		tour = Tour('destination': destination) #save needed? TODO(jisha)
		tour.fromAddress = request.POST['fromAddress']
		tour.returnAddress = request.POST['returnAddress']
		tour.startTime = request.POST['startTime']
		tour.endTime = request.POST['endTime']
		tour.save()	
		#get_json_object_from_url(destination)
		# tourId = tour.id
		tourId = 1
		return HttpResponseRedirect('/results/'+str(tourId))
	return render(request, 'home.html', {})

def results(request, tourId):
	tour = Tour.objects.get(id = tourId)
	places = Place.objects.filter(tour = tour)

	return render(request, 'results.html', {'tourId': tourId
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
				#get new places list based on areas_list	
	return render_to_response('timeline.html', places, context_instance=RequestContexxt(request))

def test(request):
	t = get_template('test.html')
	html = t.render(Context({}))
	return HttpResponse(html)
