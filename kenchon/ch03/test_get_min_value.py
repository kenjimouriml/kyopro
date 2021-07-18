import unittest
from main import get_min_value

class SearchTest(unittest.TestCase):
    
    def test_get_min_value_ok(self):
        num_list = [1, 2.8, 3, 4, 5, 6, 0.2]
        returns = get_min_value(num_list)
        
        self.assertEqual(returns, (0.2, 6))

    def test_get_min_value_typeerror(self):
        num_list = 4
        with self.assertRaises(TypeError):
            get_min_value(num_list)

    def test_get_min_value_typeerror2(self):
        num_list = [1.0, 3.0, "string"]
        with self.assertRaises(TypeError):
            get_min_value(num_list)


if __name__ == "__main__":
    unittest.main()