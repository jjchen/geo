# Create your views here
from geotours.models import Tour
from geotours.models import Area
from geotours.models import Place
from geotours.models import Transport

class SearchForm(forms.Form):


def home(request):
	# if request.method == 'POST':
	# 	form = SearchForm(request.POST)
	# 	if form.is_valid():
	# 		data = form.cleaned_data
	# 		tour = Tour()
	# 		tour.save()

	# return render(request, 'home.html', {
	# 	'form': form
	# 	})
	return render(request, 'home.html')

def results(request):
	# places = Places.objects.filter()

	# return render(request, 'results.html', {

	# 	})
	return render(request, 'results.html')