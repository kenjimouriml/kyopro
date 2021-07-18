import unittest
import numpy as np
from main import get_tribo_memo

class SearchTest(unittest.TestCase):
    
    def test_get_tribo_ok(self):
        N = 9#index
        ans = 44
        memo = - np.ones(N + 1, dtype=int)
        self.assertEqual(get_tribo_memo(N, memo), ans)
        
    def test_get_tribo_ok2(self):
        N = 1
        ans = 0
        memo = - np.ones(N + 1, dtype=int)
        self.assertEqual(get_tribo_memo(N, memo), ans)

if __name__ == "__main__":
    unittest.main()