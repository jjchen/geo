
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from geotour.models import Place

def home(request):
    t = get_template('home.html')
    html = t.render(Context({}))
    return HttpResponse(html)


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
