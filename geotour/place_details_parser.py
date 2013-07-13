import json
import urllib2
from operator import itemgetter

globallat = 37.7749295
globallng = -122.41941550000001 #San Fran

key= "AIzaSyBAKb1W6-1QgdclZMWtrYmaEHn2p2Uy2Ww"
firstU = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="
firstRadarU = "https://maps.googleapis.com/maps/api/place/radarsearch/json?location="
secondU = "&radius=50000&sensor=false&key="+key
placequery = "https://maps.googleapis.com/maps/api/place/details/json?sensor=false&key="+key

samplereference = "CoQBcwAAAA6ZWWN-e-ZS-z_UcaM5us57lPRGr1bYmY9OW3b73F5lUaET4Nbs7LBaxz5RP86Ayc4ghOvwCEQUVe18SwTWmv8ssRvS7-DIu3bnRr3_N7Pbf1NJEz2h8CTvLNtXG6N_i1CqxwSG9_vhTVIbp-lErDD0TjRvM9q-M8ugASm-26BhEhBwFWRij0Uf1LgI06u60FhqGhTYfMGXr7oq8nVWZpPB-8OqdOzA7g"
sampleplace = placequery+"&reference="+samplereference
url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=37.7749295,-122.41941550000001&radius=50000&sensor=false&key="+key
areas = { "point_of_interest": 1,
"amusement_park": 2,
"aquarium": 2,
"art_gallery": 1,
"zoo": 2,
"movie_theater": 2.5,
"museum": 1,
"bowling_alley": 2,


"food": 1,
"bakery": 0.5,
"cafe": 0.5,
"restaurant": 1,
"bar": 2,
"night_clubpark": 2,


"shopping_mall": 2,
"book_store": 1,
"clothing_store": 2,
"department_store": 2,
"jewelry_store": 1,
"spa":1
}

def getAllAreas():
  global areas
  str=""
  for area in areas:
    str=str+area+"|"
  return str[:-1]


def getUrl(lat, lng):
  global key
  global firstU
  global secondU
  url = firstU+str(lat)+","+str(lng)+secondU
  print url
  return url

def getRadarUrl(lat, lng):
  global key
  global firstU
  global secondU
  url = firstRadarU+str(lat)+","+str(lng)+secondU
  #print url
  return url

def getFromRadar(results1):
  global placequery
  results=[]
  for result in results1: 
    #print "in get from radar list"
    reference = result['reference']
    url = placequery+"&reference="+reference
    #print url
    json_object = get_json_object_from_url(url)
    if json_object['status']=="OK":
      #print json_object['result']
      results.append(json_object['result'])
  return results


#https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=37.7749295,-122.4194155&radius=50000&sensor=false&key=AIzaSyDcTs6ljMw-1EmOkjwbSbidyyGNXKhkJgc


def getPlaces(lat,lng):
  url = getUrl(lat,lng)
  json_obj = get_json_object_from_url(url)
  if json_object['status']=="OK":
    results = json_obj['results']
  else:
    results={}
  #results.sort(key=itemgetter('name'))
  for result in results:
    print result['name']
  return results

def getMultipleAreas(lat,lng,areas):
  global globallat
  global globallng
  url = getRadarUrl(lat,lng)
  url = url+"&types="+areas
  print url
  json_obj = get_json_object_from_url(url)
  results=[]
  print json_obj['status']
  if json_obj['status']=="OK":
    results1 = json_obj['results']
    results = getFromRadar(results1)

  for result in results:
    print result['name']
  return results

def getPlacesInArea(lat, lng, area):
  global areas
  global globallat
  global globallng
  print "inGetPlacesIn Area"
  url = getRadarUrl(lat,lng)
  if area in areas.keys():
    url = url+"&types="+area
  json_obj = get_json_object_from_url(url)
  results1 = json_obj['results']
  results = getFromRadar(results1)

  #results.sort(key=itemgetter('name'))
  for result in results:
    print result['name']
  return results


def get_json_object_from_url(url):
  """Given a url of a query, returns an object with the results.

  Args:
    url: string, the url representing a query.

  Returns:
    Python object representing the JSON result.
  """

  JSON_text = urllib2.urlopen(url).read()
  JSON_decoder = json.JSONDecoder()
  JSON_object = JSON_decoder.decode(JSON_text)
  return JSON_object


def createPlaceRequest():
  global key
  global firstU
  global secondU

def tony():
  """
  Example usage:

  json_object = get_json_object_from_url('https://something.blah.com/blahblahblah')
  json_object['results'][0]['name']  # gives the name of the first result
  json_object['results'][0]['rating']  # gives the rating of the first result
  """

  json_obj = get_json_object_from_url('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=37.7749295,-122.41941550000001&radius=50000&sensor=false&point_of_interest&key=AIzaSyDcTs6ljMw-1EmOkjwbSbidyyGNXKhkJgc')

  results = json_obj['results']



  from operator import itemgetter
  #results.sort(key=itemgetter('name'))

  for result in results:
    print result['name']

def getResultsFromObject(json_object):
  results = json_obj['results']
  #results.sort(key=itemgetter('name'))
  for result in results:
    print result['name']


#results = getPlacesInArea(37.7749295,-122.41941550000001, "movie_theatre")
results = getMultipleAreas(37.7749295,-122.41941550000001, getAllAreas())
# url = getUrl(37.7749295,-122.41941550000001)
# # JSON = get_json_object_from_url(url)
# results=  JSON['results']



