import unittest
import numpy as np
from main import dp_napsack


class SearchTest(unittest.TestCase):

    def test_nap_sack_ok(self):
        """
        https://blog.brainpad.co.jp/entry/2020/10/09/000002
        """
        w = [75, 70, 90, 60, 120, 125, 185, 205, 175, 270, 315]
        v = [7, 6, 10, 10, 22, 17, 23, 27, 20, 33, 36]
        w_const = 500

        self.assertEqual(dp_napsack(v, w, w_const), 72)


if __name__ == "__main__":
    unittest.main()
