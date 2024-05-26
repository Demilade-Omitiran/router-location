import unittest

from src.network import Network
from src.router import Router
from src.location import Location

class TestNetwork(unittest.TestCase):
  def test_network_initialization(self):
    routers = [
      {"id": 1, "name": "citadel-01", "location_id": 2, "router_links": [2, 3]},
      {"id": 2, "name": "citadel-02", "location_id": 3, "router_links": [1]},
      {"id": 3, "name": "core-07", "location_id": 1, "router_links": [1]}
    ]

    locations = [
      {"id": 1, "postcode": "BE12 2ND", "name": "Birmingham Motorcycle Museum"},
      {"id": 2, "postcode": "BE12 2ND", "name": "Birmingham Hippodrome"},
      {"id": 3, "postcode": "BE13 1EQ", "name": "Winterbourne House"}
    ]

    network = Network(routers, locations)
    self.assertEqual(len(network.routers), 3)
    self.assertEqual(len(network.locations), 3)
    self.assertEqual(network.routers[0].id, routers[0]["id"])
    self.assertEqual(network.routers[0].name, routers[0]["name"])
    self.assertEqual(network.routers[0].location_id, routers[0]["location_id"])
    self.assertEqual(network.routers[0].links, routers[0]["router_links"])
    self.assertTrue(isinstance(network.routers[0], Router))
    self.assertEqual(network.locations[0].id, locations[0]["id"])
    self.assertEqual(network.locations[0].name, locations[0]["name"])
    self.assertEqual(network.locations[0].postcode, locations[0]["postcode"])
    self.assertTrue(isinstance(network.locations[0], Location))

if __name__ == "__main__":
  unittest.main()