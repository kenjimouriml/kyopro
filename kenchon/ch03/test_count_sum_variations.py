import unittest
from main import count_sum_variations

class SearchTest(unittest.TestCase):
    
    def test_count_sum_variations_ok(self):
        N = 10
        K = 5
        self.assertEqual(count_sum_variations(N, K), 5)
        
    def test_count_sum_variations_ok2(self):
        N = 10
        K = 3
        self.assertEqual(count_sum_variations(N, K), 0)

    def test_count_sum_variations_ok3(self):
        N = 10
        K = 10
        self.assertEqual(count_sum_variations(N, K), 14)

if __name__ == "__main__":
    unittest.main()