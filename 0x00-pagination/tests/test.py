import unittest
index_range = __import__('0-simple_helper_function').index_range

class TestIndexRange(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(index_range(1, 10), (0, 10))

    def test_case_2(self):
        self.assertEqual(index_range(2, 10), (10, 20))

    def test_case_3(self):
        self.assertEqual(index_range(3, 10), (20, 30))

    def test_case_4(self):
        self.assertEqual(index_range(0, 10), (0, 10))

    def test_case_5(self):
        self.assertEqual(index_range(1, 0), (0, 0))

if __name__ == '__main__':
    unittest.main()