import unittest
from src.location import Location

class TestLocation(unittest.TestCase):
  def test_location_initialization(self):
    location = Location(1, "Birmingham", "B21 ABC")
    self.assertEqual(location.id, 1)
    self.assertEqual(location.name, "Birmingham")
    self.assertEqual(location.postcode, "B21 ABC")

if __name__ == "__main__":
  unittest.main()