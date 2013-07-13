

from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

def home(request):
    t = get_template('home.html')
    html = t.render(Context({}))
    return HttpResponse(html)
    # latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    # context = {'latest_poll_list': latest_poll_list}
    # return render(request, 'polls/index.html', context)


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
	# places = Places.objects.filter()

	# return render(request, 'results.html', {

	# # 	})
	# return render(request, 'results.html')


    t = get_template('results.html')
    html = t.render(Context({}))
    return HttpResponse(html)

def test(request):
	t = get_template('test.html')
	html = t.render(Context({}))
	return HttpResponse(html)
