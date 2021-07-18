import unittest
import numpy as np
from main import get_fibo_memo

class SearchTest(unittest.TestCase):
    
    def test_get_fibo_ok(self):
        N = 10#index
        ans = 55
        memo = - np.ones(N + 1, dtype=int)
        self.assertEqual(get_fibo_memo(N, memo), ans)
        
    def test_get_fibo_ok2(self):
        N = 1
        ans = 1
        memo = - np.ones(N + 1, dtype=int)
        self.assertEqual(get_fibo_memo(N, memo), ans)

if __name__ == "__main__":
    unittest.main()