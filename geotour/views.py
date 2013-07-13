
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from geotour.models import Place
from django.template.defaulttags import csrf_token

include place_details_parser.py

def home(request):
	if request.method == 'POST':
		destination = 
		tour = Tour('destination': request.POST['destination']) #save needed? TODO(jisha)
		tour.fromAddress = request.POST['fromAddress']
		tour.returnAddress = request.POST['returnAddress']
		tour.startTime = request.POST['startTime']
		tour.endTime = request.POST['endTime']
		tour.save()	
		get_json_object_from_url()
		return HttpResponseRedirect('/results')
	return render(request, 'home.html', {})



# class SearchForm(forms.Form):


# def home(request):
# 	# if request.method == 'POST':
# 	# 	form = SearchForm(request.POST)
# 	# 	if form.is_valid():
# 	# 		data = form.cleaned_data
# 	# 		tour = Tour()
# 	# 		tour.save()

# 	# return render(request, 'home.html', {
# 	# 	'form': form
# 	# 	})
# 	return render(request, 'home.html')

def results(request):
	places = Place.objects.all()
	return render(request, 'results.html', {
		'places': places
		})

def test(request):
	t = get_template('test.html')
	html = t.render(Context({}))
	return HttpResponse(html)
