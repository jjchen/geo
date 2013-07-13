
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from geotour.models import Place
from geotour.models import Tour
from django.template.defaulttags import csrf_token

def home(request):
	if request.method == 'POST':
		# destination = request.POST['destination']
		# tour = Tour('name': request.POST['name'])
		# tour.save()
		# tourId = tour.id
		tourId = 1
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
	return render_to_response('timeline.html', places, context_instance=RequestContexxt(request))

def test(request):
	t = get_template('test.html')
	html = t.render(Context({}))
	return HttpResponse(html)
