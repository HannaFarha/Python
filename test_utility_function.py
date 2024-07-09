from unittest import TestCase
from utility_function import div

class Test(TestCase):
    def test_div(self):
        self.assertEqual(2,div(6,3))
        self.assertEqual(0, div(6, 0))
        self.assertEqual(1, div(6, 4))
