import json
import urllib2

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

"""
Example usage:

json_object = get_json_object_from_url('https://something.blah.com/blahblahblah')
json_object['results'][0]['name']  # gives the name of the first result
json_object['results'][0]['rating']  # gives the rating of the first result
"""

json_obj = get_json_object_from_url('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=37.7749295,-122.41941550000001&radius=50000&sensor=false&point_of_interest&key=AIzaSyDcTs6ljMw-1EmOkjwbSbidyyGNXKhkJgc')

results = json_obj['results'][:50]

from operator import itemgetter
#results.sort(key=itemgetter('name'))

for result in results:
	print result['name']
