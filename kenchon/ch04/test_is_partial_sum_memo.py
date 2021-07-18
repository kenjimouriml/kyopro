import unittest
import numpy as np
from main import is_partial_sum_memo

class SearchTest(unittest.TestCase):
    
    def test_is_partial_sum_ok(self):
        array = [1, 2, 4, 5, 11]
        W = 10
        d = abs(W - np.sum(array))
        memo = - np.ones((len(array), W + d))
        self.assertTrue(
            is_partial_sum_memo(array, len(array), W, memo, d))
        
    def test_is_partial_sum_ok2(self):
        array = [1, 5, 8, 11]
        W = 10
        d = abs(W - np.sum(array))
        memo = - np.ones((len(array), W + d))
        self.assertFalse(
            is_partial_sum_memo(array, len(array), W, memo, d))

if __name__ == "__main__":
    unittest.main()