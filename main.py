import requests
from src.network import Network

url = "https://my-json-server.typicode.com/marcuzh/router_location_test_api/db"
response = requests.get(url)
data = response.json()

def main():
  network = Network(data["routers"], data["locations"])
  network.generate_connected_locations()
  print_dashes()
  network.print_directly_connected_locations()
  print_dashes()
  network.print_directly_connected_locations_and_routers()
  print_dashes()

def print_dashes():
  print("---------------------------------------------------------------------------")

main()