from typing import List, Tuple
import itertools
import numpy as np


def calc_frog_v1(N: int, array: List[int]) -> int:

    dp = np.ones(N) * 100000000
    dp[0] = 0
    dp[1] = dp[0] + abs(array[1] - array[0])

    for i in range(2, N):
        dp[i] = min(dp[i - 1] + abs(array[i] - array[i - 1]),
                    dp[i - 2] + abs(array[i] - array[i - 2]))

    return dp[N-1]


def calc_frog_v2(N: int, array: List[int]) -> int:

    def chmin(val_current, val_new):
        if val_current > val_new:
            val_current = val_new
        return val_current

    dp = np.ones(N) * 1000000000
    dp[0] = 0

    for i in range(1, N):
        dp[i] = chmin(dp[i], dp[i - 1] + abs(array[i] - array[i - 1]))
        if i > 1:
            dp[i] = chmin(dp[i], dp[i - 2] + abs(array[i] - array[i - 2]))

    return dp[N-1]


def calc_frog_v3(N: int, arr: List[int]) -> int:

    def chmin(val_current, val_new):
        if val_current > val_new:
            val_current = val_new
        return val_current

    dp = np.ones(N) * 1000000000
    dp[0] = 0

    for i in range(0, N - 2):
        dp[i + 1] = chmin(dp[i + 1],
                          dp[i] + abs(arr[i + 1] - arr[i]))
        dp[i + 2] = chmin(dp[i + 2],
                          dp[i] + abs(arr[i + 2] - arr[i]))
        if i == N - 3:
            dp[i + 2] = chmin(dp[i + 2],
                              dp[i + 1] + abs(arr[i + 2] - arr[i + 1]))

    return dp[N-1]


def calc_frog_rec(N: int, arr: List[int]) -> int:
    """
    N : index
    """
    if N == 0:
        return 0
    if N == 1:
        return abs(arr[1] - arr[0])

    res = 10000000000
    res = min(res,
              calc_frog_rec(N - 1, arr) + abs(arr[N] - arr[N - 1]))

    res = min(res,
              calc_frog_rec(N - 2, arr) + abs(arr[N] - arr[N - 2]))

    return res


def calc_frog_rec_memo(N: int, arr: List[int],
                       dp: List[int]) -> int:
    """
    N : index
    """
    if N == 0:
        return 0
    if N == 1:
        return abs(arr[1] - arr[0])

    if dp[N] != -1:
        return dp[N]
    else:
        res = 10000000000
        dp[N] = min(res,
                    calc_frog_rec_memo(N - 1, arr, dp) +
                    abs(arr[N] - arr[N - 1]))

        dp[N] = min(dp[N],
                    calc_frog_rec_memo(N - 2, arr, dp) +
                    abs(arr[N] - arr[N - 2]))

        return dp[N]


def dp_napsack(v: List[int], w: List[int], w_const: int) -> int:

    dp = np.zeros((len(v), w_const), dtype=int)

    for i in range(len(v) - 1):
        for j in range(w_const):

            if j - w[i] >= 0:
                dp[i + 1, j] = max(
                    dp[i + 1, j], dp[i, j - w[i]] + v[i]
                )

            dp[i + 1, j] = max(dp[i + 1, j], dp[i][j])

    return dp[len(v) - 1, w_const - 1]
