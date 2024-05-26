from src.router import Router
from src.location import Location

class Network:
  def __init__(self, routers, locations):
    self.routers = { router['id']: Router(router['id'], router['name'], router['location_id'], router['router_links']) for router in routers }
    self.locations = { location['id']: Location(location['id'], location['name'], location['postcode']) for location in locations }
    self.direct_connections = { "locations": set(), "locations_and_routers": {} }

  def generate_connected_locations(self):
    self.generate_directly_connected_locations()

  def generate_directly_connected_locations(self):
    for router in self.routers.values():
      for link in router.links:
        link_location_id = self.routers[link].location_id
        connected_location = tuple(sorted([router.location_id, link_location_id]))
        self.direct_connections["locations"].add(connected_location)
        connected_location_key = str(connected_location)
        routers_value = tuple(sorted([router.id, link]))
        if connected_location_key not in self.direct_connections["locations_and_routers"]:
          self.direct_connections["locations_and_routers"][connected_location_key] = set()
        self.direct_connections["locations_and_routers"][connected_location_key].add(routers_value)

  def print_directly_connected_locations(self):
    print("Directly-Connected Locations:")
    for connection in self.direct_connections["locations"]:
      location_1, location_2 = self.locations[connection[0]].name, self.locations[connection[1]].name
      print(f"{location_1} <-> {location_2}")