import unittest
from main import count_divs

class SearchTest(unittest.TestCase):
    
    def test_count_divs_ok(self):
        num_list = [2**3, 2**4, 2**5, 2**6, 2**7, 2**8]
        divs = 3
        self.assertEqual(count_divs(num_list), divs)

    def test_count_divs_ok2(self):
        num_list = [19, 2**4, 2**5, 2**6, 2**7, 2**8]
        divs = 0
        self.assertEqual(count_divs(num_list), divs)

if __name__ == "__main__":
    unittest.main()