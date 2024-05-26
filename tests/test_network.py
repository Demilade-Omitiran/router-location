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
    self.assertEqual(network.direct_connections, { "locations": set(), "locations_and_routers": {} })
    self.assertEqual(network.routers[routers[0]["id"]].id, routers[0]["id"])
    self.assertEqual(network.routers[routers[0]["id"]].name, routers[0]["name"])
    self.assertEqual(network.routers[routers[0]["id"]].location_id, routers[0]["location_id"])
    self.assertEqual(network.routers[routers[0]["id"]].links, routers[0]["router_links"])
    self.assertIsInstance(network.routers[routers[0]["id"]], Router)
    self.assertEqual(network.locations[locations[0]["id"]].id, locations[0]["id"])
    self.assertEqual(network.locations[locations[0]["id"]].name, locations[0]["name"])
    self.assertEqual(network.locations[locations[0]["id"]].postcode, locations[0]["postcode"])
    self.assertIsInstance(network.locations[locations[0]["id"]], Location)

  def test_generate_directly_connected_locations(self):
    routers = [
      {"id": 1, "name": "citadel-01", "location_id": 2, "router_links": [2, 3, 4]},
      {"id": 2, "name": "citadel-02", "location_id": 3, "router_links": [1, 2]},
      {"id": 3, "name": "core-07", "location_id": 1, "router_links": [1]},
      {"id": 4, "name": "core-07", "location_id": 1, "router_links": [1]}
    ]

    locations = [
      {"id": 1, "postcode": "BE12 2ND", "name": "Birmingham Motorcycle Museum"},
      {"id": 2, "postcode": "BE12 2ND", "name": "Birmingham Hippodrome"},
      {"id": 3, "postcode": "BE13 1EQ", "name": "Winterbourne House"}
    ]

    expected_direct_connections = { 
      "locations": { (1,2), (2,3), (3,3) },
      "locations_and_routers": {
        "(1, 2)": { (1,3), (1,4) },
        "(2, 3)": { (1,2) },
        "(3, 3)": { (2,2) },
      }
    }

    network = Network(routers, locations)
    network.generate_connected_locations()
    self.assertEqual(len(network.direct_connections["locations"]), 3)
    self.assertSetEqual(expected_direct_connections["locations"], network.direct_connections["locations"])
    self.assertDictEqual(expected_direct_connections["locations_and_routers"], network.direct_connections["locations_and_routers"])

if __name__ == "__main__":
  unittest.main()