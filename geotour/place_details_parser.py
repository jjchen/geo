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
