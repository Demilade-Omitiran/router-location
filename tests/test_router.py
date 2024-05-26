import unittest
from src.router import Router

class TestRouter(unittest.TestCase):
  def test_router_initialization(self):
    router = Router(1, "This Router", 1, [2, 3])
    self.assertEqual(router.id, 1)
    self.assertEqual(router.name, "This Router")
    self.assertEqual(router.location_id, 1)
    self.assertEqual(router.links, [2, 3])

if __name__ == "__main__":
  unittest.main()