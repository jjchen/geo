# -*- coding: utf-8 -*-

from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from geotour.models import Place
from geotour.models import Tour
from django.template.defaulttags import csrf_token
import datetime
import pusher
from place_details_parser import *

lat = 37.7749295
lng = -122.41941550000001

p = pusher.Pusher(
    app_id='51495',
    key='f716260bfec4431cf252',
    secret='56b567413491c2c0e8d4'
)

def home(request):
    global lat
    global lng
    if request.method == 'POST':
        destination = request.POST['destination']

        tour = Tour.objects.create(destination=destination) #save needed? TODO(jisha)
        tour.save()
        # latlng= LatLngs.objects.create(tour=tour)
        tour.fromAddress = request.POST['fromAddress']
        tour.returnAddress = request.POST['returnAddress']
        lat = request.POST['lat']
        lng = request.POST['lng']
        print lat
        print lng
        # latlng.save()
        fmt = '%m/%d/%Y %I:%M%p'
        date = request.POST['date']
        startTime = request.POST['startTime']
        endTime = request.POST['endTime']
        if date is None or date.strip()=="":
            print "date is blank!!!!!!!!!!!!!!!!!!!!!!!!"
            date = "07/13/2013"
        if startTime is None or startTime.strip()=="":
            startTime = "9:00AM"
        if endTime is None or endTime.strip()=="":
            endTime = startTime
        d = datetime.datetime.strptime(date+" "+startTime, fmt)
        tour.startTime = d
        # d = datetime.datetime.strptime(request.POST['date']+" "+ endTime, fmt)
        # tour.startTime = request.POST['startTime']
        # tour.endTime = request.POST['endTime']
        tour.save() 
        # latlng.save()
        #get_json_object_from_url(destination)
        tourId = tour.id
        # tourId = 1 #take this out
        return HttpResponseRedirect('/results/'+str(tourId))
    return render(request, 'home.html', {})
  
def addDefaults(arg):
    #defaults = getDefaults() 
    return arg 

# def results(request, tourId):
#   tour = Tour.objects.get(id = tourId)
#   placedict={}
#     for item in getPlaces(lat, lng):
#       placedict['location'] = item['geometry']
#       placedict['name'] = item['name']

#   #places = Place.objects.filter(tour = tour)
#   return render(request, 'home.html', {})


def update(request):
    global lat
    global lng
    return render(request, 'results.html', {})

def results(request, tourId):
    global lat
    global lng
    tour = Tour.objects.get(id = tourId)
    placedict={}
    p = Place.objects.filter(tour = tour)
    p.delete()
    places = []
    placesresults = getPlaces(lat, lng)
    placesresults =  addDefaults(placesresults);
    for item in placesresults:
        place = Place.objects.create(tour = tour)
        place.name = item['name']
        place.address = item['geometry']['location']['lat']
        place.details = item['geometry']['location']['lng']
        print place.name
        print place.address
    	place.save()
    places = Place.objects.filter(tour = tour)
    searchResults = []
    tourPlaces = []
    return render(request, 'results.html', {'tourId': tourId,
        'searchResults': places, 'tourPlaces': places
        })

def change(request):
    global lat
    global lng
    print "change"
    tourId = request.POST['tourId']
    wholeList = request.POST.getlist('areas')
    split = wholeList[0].split('&')
    areas = []
    for areaOn in split:
        area = areaOn.split('=')
        if area[1] == 'on':
            areas.append(area[0])

    searchResults = []
    tourPlaces = []

    tour = Tour.objects.get(id = tourId)
    p = Place.objects.filter(tour = tour)
    p.delete()
    places = []
    if areas != None and len(areas) != 0:
        areas_list = []
        for area in areas:
            search = getPlacesInArea(lat, lng, area)
            for item in search:
                place = Place.objects.create(tour = tour)
                place.name = item['name']
                place.address = item['geometry']['location']['lat']
                place.details = item['geometry']['location']['lng']

                place.save()

                searchResults.append(place)
                tourPlaces.append(place)
    p['tour' + str(tourId)].trigger('change', {})
    return render(request, 'timeline.html', {'tourId': tourId,
        'searchResults': searchResults, 'tourPlaces': tourPlaces
        })

def update(request):
    tourId = request.POST['tourId']
    tour = Tour.objects.get(id = tourId)
    p = Place.objects.filter(tour = tour)
    for place in p:
        searchResults.append(place)
        tourPlaces.append(place)
    return render(request, 'timeline.html', {'tourId': tourId,
        'searchResults': searchResults, 'tourPlaces': tourPlaces
        }) 

def test(request):
    t = get_template('test.html')
    html = t.render(Context({}))
    return HttpResponse(html)
