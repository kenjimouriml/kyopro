import unittest
import numpy as np
from main import is_partial_sum

class SearchTest(unittest.TestCase):
    
    def test_is_partial_sum_ok(self):
        array = [1, 2, 4, 5, 11]
        W = 10
        self.assertTrue(is_partial_sum(array, len(array), W))
        
    def test_is_partial_sum_ok2(self):
        array = [1, 5, 8, 11]
        W = 10
        self.assertFalse(is_partial_sum(array, len(array), W))

if __name__ == "__main__":
    unittest.main()