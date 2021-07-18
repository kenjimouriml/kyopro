import unittest
from main import get_min_pair

class SearchTest(unittest.TestCase):
    
    def test_get_min_pair_ok(self):
        num_list1 = [1, 2, 3, 4, 5, 6]
        num_list2 = [7, 2, 19, 4, 5, 3]
        K = 15
        
        self.assertEqual(get_min_pair(num_list1, num_list2, K), 20)

    def test_get_min_pair_K(self):
        num_list1 = [1, 2, 3, 4, 5, 6]
        num_list2 = [7, 2, 19, 4, 5, 3]
        K = 90

        self.assertEqual(get_min_pair(num_list1, num_list2, K), K)

    def test_get_min_value_typeerror1(self):
        num_list1 = [1, 2, 3, 4, 5, 6]
        num_list2 = 5
        K = 90

        with self.assertRaises(TypeError):
            get_min_pair(num_list1, num_list2, K)

    def test_get_min_value_typeerror2(self):
        num_list1 = 3
        num_list2 = [1, 2, 3, 4, 5, 6]
        K = 90

        with self.assertRaises(TypeError):
            get_min_pair(num_list1, num_list2, K)

    def test_get_min_value_typeerror3(self):
        num_list1 = [1, 2, 3, 4, 5, 6]
        num_list2 = [1, 2, 3, 4, 5, 6]
        K = [1, 3]

        with self.assertRaises(TypeError):
            get_min_pair(num_list1, num_list2, K)

    def test_get_min_value_typeerror4(self):
        num_list1 = [1, 2, 3, 4, "string", 6]
        num_list2 = [1, 2, 3, 4, 5, 6]
        K = 5

        with self.assertRaises(TypeError):
            get_min_pair(num_list1, num_list2, K)

    def test_get_min_value_typeerror5(self):
        num_list1 = [1, 2, 3, 4, 5, 6]
        num_list2 = [1, 2, 3, 4, "string", 6]
        K = 5

        with self.assertRaises(TypeError):
            get_min_pair(num_list1, num_list2, K)

    def test_get_min_value_typeerror6(self):
        num_list1 = [1, 2, 3, 4, 5, 6]
        num_list2 = [1, 2, 3, 4, 5, 6]
        K = "string"

        with self.assertRaises(TypeError):
            get_min_pair(num_list1, num_list2, K)


if __name__ == "__main__":
    unittest.main()