from math import sin, cos, radians, acos

# http://en.wikipedia.org/wiki/Earth_radius
# """For Earth, the mean radius is 6,371.009 km (~3,958.761 mi)"""
EARTH_RADIUS_IN_MILES = 3958.761

def calc_dist(lat_a, long_a, lat_b, long_b):
    """all angles in degrees, result in miles"""
    lat_a = radians(lat_a)
    lat_b = radians(lat_b)
    delta_long = radians(long_a - long_b)
    cos_x = (
        sin(lat_a) * sin(lat_b) +
        cos(lat_a) * cos(lat_b) * cos(delta_long)
        )
    return acos(cos_x) * EARTH_RADIUS_IN_MILES

# Austin to San Fransisco
print calc_dist(30.267153, -97.74306079999997, 37.7749295, -122.41941550000001)
