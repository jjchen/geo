from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

def home(request):
    t = get_template('home.html')
    html = t.render(Context({}))
    return HttpResponse(html)

def results(request):
    t = get_template('results.html')
    html = t.render(Context({}))
    return HttpResponse(html)