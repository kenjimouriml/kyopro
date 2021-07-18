import unittest
from main import is_partial_sum

class SearchTest(unittest.TestCase):
    
    def test_is_partial_sum_ok(self):
        num_list = [1, 2, 3, 4, 5, 6]
        W = 8
        self.assertTrue(is_partial_sum(num_list, W))
        
    def test_is_partial_sum_ok2(self):
        num_list = [1, 2, 3, 4, 5, 6]
        W = 22
        self.assertFalse(is_partial_sum(num_list, W))

    def test_is_partial_sum_typeerror(self):
        num_list = 1
        W = 22
        with self.assertRaises(TypeError):
            is_partial_sum(num_list, W)

if __name__ == "__main__":
    unittest.main()