import unittest
import numpy as np
from main import calc_frog_rec_memo


class SearchTest(unittest.TestCase):

    def test_calc_frog_ok(self):
        array = [2, 9, 4, 5, 1, 6, 10]
        memo = - np.ones(len(array))
        N = 6
        self.assertEqual(calc_frog_rec_memo(N, array, memo), 8)


if __name__ == "__main__":
    unittest.main()
