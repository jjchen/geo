from place_details_parser import get_json_object_from_url

def get_movies(date, zip_code=None, lat=None, lon=None, radius=None):
  """Gets a movie in the format described at:
  http://developer.tmsapi.com/docs/read/data_v1/movies/Movie_showtimes_by_zip_code.

  Args:
    date: string in 'yyyy-mm-dd'. Current date or greater.
    zip_code: int (please enter zip or lat/lon).
    lat: double (please enter zip or lat/lon).
    lon: double (please enter zip or lat/lon).
    radius: int, range to look in miles (default = 5).
  """
  url = 'http://data.tmsapi.com/v1/movies/showings?startDate=' + date
  if zip_code:
    url += '&zip=' + str(zip_code)
  elif lat and lon:
    url += '&lat=' + str(lat) + '&lon=' + str(lon)
  else:
    # No location was passed!
    return None
  if radius:
    url += '&radius=' + str(radius)
  url += '&api_key=zczrj7uyushqt8yd9tdpvnp6'
  return get_json_object_from_url(url)

"""
Sample usage:
movies = get_movies('2013-07-13', zip_code=95134)
print len(movies)  # Number of movies playing in the area.
print movies[0]['title']
# Note the spelling of 'theatre'...
print movies[0]['showtimes'][0]['theatre']['name']
"""
