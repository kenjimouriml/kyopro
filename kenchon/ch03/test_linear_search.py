import unittest
from main import linear_search

class SearchTest(unittest.TestCase):
    
    def test_linear_search_ok(self):
        num_list = [1, 2, 3, 4, 5, 6]
        target = 3

        returns = linear_search(num_list, target)
    
        self.assertTrue(returns[0])
        self.assertEqual(returns[1], 2)

    def test_linear_search_typeerror(self):
        num_list = 3
        target = 3
        with self.assertRaises(TypeError):
            linear_search(num_list, target)

    def test_linear_search_ok2(self):
        num_list = [1, 2, 3, 4, 5, 6]
        target = 9
        returns = linear_search(num_list, target)
    
        self.assertFalse(returns[0])
        self.assertEqual(returns[1], -1)


    def test_linear_search_type(self):
        num_list = [1, 2, 3, 4, 5, 6]
        target = 5.8
        
        returns = linear_search(num_list, target)
    
        self.assertFalse(returns[0])
        self.assertEqual(returns[1], -1)


if __name__ == "__main__":
    unittest.main()