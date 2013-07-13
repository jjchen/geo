import json
import urllib2
from operator import itemgetter

key= "AIzaSyDcTs6ljMw-1EmOkjwbSbidyyGNXKhkJgc"
firstU = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location"
secondU = "&radius=50000&sensor=false&point_of_interest&key="+key
url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=37.7749295,-122.41941550000001&radius=50000&sensor=false&point_of_interest&key="+key

def getUrl(lat, lng):
  global key
  global firstU
  global secondU
  url = firstU+str(lat)+","+str(lng)+secondU
  print url
  return url


def getPlaces(lat,lng):
  url = getUrl(lat,lng)
  json_object = get_json_object_from_url(url)
  results = getResultsFromObject(json_object)
  #results.sort(key=itemgetter('name'))
  for result in results:
    print result['name']

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



url = getUrl(37.7749295,-122.41941550000001)
JSON = get_json_object_from_url(url)
results=  JSON['results']



