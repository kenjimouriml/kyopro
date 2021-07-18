import unittest
from main import sum_Ndigit_numbers

class SearchTest(unittest.TestCase):
    
    def test_sum_Ndigit_numbers_ok(self):
        num = "125"
        total = 176
        self.assertEqual(sum_Ndigit_numbers(num), total)
        
    def test_sum_Ndigit_numbers_ok2(self):
        num = "1"
        total = 1
        self.assertEqual(sum_Ndigit_numbers(num), total)

if __name__ == "__main__":
    unittest.main()