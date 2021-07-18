import unittest
from main import gcd

class SearchTest(unittest.TestCase):
    
    def test_gcd_ok(self):
        num_1 = 12
        num_2 = 8
        ans = 4
        self.assertEqual(gcd(num_1, num_2), ans)
        
    def test_gcd_ok2(self):
        num_1 = 1
        num_2 = 1
        ans = 1
        self.assertEqual(gcd(num_1, num_2), ans)

    def test_gcd_ok3(self):
        num_1 = 8
        num_2 = 12
        ans = 4
        self.assertEqual(gcd(num_1, num_2), ans)

if __name__ == "__main__":
    unittest.main()