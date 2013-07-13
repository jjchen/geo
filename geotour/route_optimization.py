class route_optimization(object):
  def __init__(self, travel_times):
    """
    Args: travel_times: {(string, string): double}, maps (start_loc, end_loc)
        to the time needed to travel between them in minutes.
    """
    self.travel_times = travel_times
    # Let's assume reverse direction takes the same amount of time.
    for leg in self.travel_times.keys():
      self.travel_times[(leg[1], leg[0])] = self.travel_times[leg]
    # Maps time in minutes to route permutations (lists of strings). It's okay
    # if a route gets overwritten by an equally fast route in this case.
    self.route_times = {}
  def optimize_route(self, origin, destinations):
    """Gives the order of destinations that will result in the least travel time.

    Args:
      origin: string, the starting location.
      destinations: list of strings, the locations to visit.

    Returns:
      list of destination strings in optimized order.
    """
    initial_route = [origin]
    self.generate_route_times(initial_route, destinations)
    return self.route_times[min(self.route_times.keys())]
  def generate_route_times(self, current_route, remaining_destinations):
    """Recursively adds route permutations to self.route_times.
    Args:
      current_route: list of strings that have been used for this permutation.
      remaining_destinations: list of strings remaining.
    """
    n = len(remaining_destinations)
    if n == 1:
      final_route = current_route + remaining_destinations
      # Add this complete permutation to the 
      self.route_times[self.get_time(final_route)] = final_route
    else:
      for x in range(n):
        new_route = current_route + [remaining_destinations[x]]
        destinations_left = remaining_destinations[:x] + remaining_destinations[x+1:]
        self.generate_route_times(new_route, destinations_left)
  def get_time(self, route):
    result = 0
    for x in range(len(route) - 1):
      result += self.travel_times[(route[x], route[x + 1])]
    return result

"""
Sample usage:
a = 'San Jose'
b = 'San Francisco'
c = 'Santa Cruz'
x = route_optimization({(a,b): 60, (a,c): 45, (b,c): 75})

# Note: generate_route_times is generally a private function.
x.generate_route_times([a], [b,c])
print x.route_times

# This is the function you should call.
print x.optimize_route(a, [b,c])
"""

