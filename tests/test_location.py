import unittest

from src.location import Location

class TestRouter(unittest.TestCase):
  def test_location_initialization(self):
    location = Location(1, "Birmingham")
    self.assertEqual(location.location_id, 1)
    self.assertEqual(location.name, "Birmingham")

if __name__ == "__main__":
  unittest.main()