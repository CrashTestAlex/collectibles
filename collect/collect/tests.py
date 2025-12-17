from django.test import TestCase
from .models import Collectible

class CMTests(TestCase):
    def test_collectible_creation(self):
        c = Collectible.objects.create(
            name="Test Item",
            emoji=123, # add working ID
            image_url="https://avatars.githubusercontent.com/u/200025324?v=4",
            cost=50,
            requirement_type="total",
            requirement_value="10", # own 10 total balls
        )
        self.assertEqual(c.name, "Test Item")
        self.assertEqual(c.emoji, 123)
        self.assertEqual(c.cost, 50)
        self.assertEqual(c.requirement_type, "total")
        self.assertEqual(c.requirement_value, "10")
        self.assertIn("Test Item", str(c))

