
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from geotour.models import Place

def home(request):
	if request.method == 'POST':
		# destination = request.POST['destination']
		# tour = Tour('name': request.POST['name'])
		# tour.save()
		return HttpRequestRedirect('/results')
	t = get_template('home.html')
	html = t.render(Context({}))
	return HttpResponse(html)

def results(request):
	places = Place.objects.all()
	return render(request, 'results.html', {
		'places': places
		})

def test(request):
	t = get_template('test.html')
	html = t.render(Context({}))
	return HttpResponse(html)
