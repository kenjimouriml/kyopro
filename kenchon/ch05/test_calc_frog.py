import unittest
import numpy as np
from main import calc_frog_v3


class SearchTest(unittest.TestCase):

    def test_calc_frog_ok(self):
        array = [2, 9, 4, 5, 1, 6, 10]
        N = 7
        self.assertEqual(calc_frog_v3(N, array), 8)


if __name__ == "__main__":
    unittest.main()
