import unittest
from app import add

class TestApp(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 20), 30)

    def test_add2(self):
        self.assertEqual(add(5, 5), 10)

if __name__ == '__main__':
    unittest.main()
