import unittest
from main import set_search

class SearchTest(unittest.TestCase):
    
    def test_linear_search_ok(self):
        num_list = [1, 2, 3, 4, 5, 6]
        target = 3
        self.assertTrue(set_search(num_list, target))
        
    def test_linear_search_ng(self):
        num_list = [1, 2, 3, 4, 5, 6]
        target = 9
        self.assertFalse(set_search(num_list, target))

    def test_linear_search_ng2(self):
        num_list = 4
        target = 9
        with self.assertRaises(TypeError):
            set_search(num_list, target)

    def test_linear_search_type(self):
        num_list = [1, 2, 3, 4, 5, 6]
        target = 5.8
        self.assertFalse(set_search(num_list, target))


if __name__ == "__main__":
    unittest.main()