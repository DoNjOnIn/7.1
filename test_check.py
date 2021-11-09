import unittest
from main import checknum

class MyTestCase(unittest.TestCase):
    def test_max(self):
        self.assertEqual(checknum('33'),True)
