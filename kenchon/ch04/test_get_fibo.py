import unittest
from main import get_fibo

class SearchTest(unittest.TestCase):
    
    def test_get_fibo_ok(self):
        N = 7#index
        ans = 13
        self.assertEqual(get_fibo(N), ans)
        
    def test_get_fibo_ok2(self):
        N = 1
        ans = 1
        self.assertEqual(get_fibo(N), ans)

if __name__ == "__main__":
    unittest.main()