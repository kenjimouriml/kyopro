from typing import List, Tuple
import itertools
import numpy as np

def gcd(num_1: int, num_2: int) -> int:

    if num_1 < num_2:
        _dum = num_1
        num_1 = num_2
        num_2 = _dum

    if num_2 == 0:
        return num_1
    
    return gcd(num_2, num_1 % num_2)


def get_fibo(N: int) -> int:
    """
    N : index 
    """

    if N == 0:
        return 0
    if N == 1:
        return 1

    return get_fibo(N-1) + get_fibo(N-2)

def get_fibo_memo(N: int, memo: List[int]) -> int:
    """
    N : index 
    """

    if N == 0:
        return 0
    if N == 1:
        return 1

    if memo[N] != -1:
        return memo[N]
    else:
        memo[N] = get_fibo_memo(N - 1, memo) + get_fibo_memo(N - 2, memo)
        return memo[N]

def is_partial_sum(array: List[int], i: int, W: int) -> bool:
    if i == 0 and W == 0:
        return True
    if i == 0 and W != 0:
        return False

    return is_partial_sum(array, i - 1, W) + is_partial_sum(array, i - 1, W - array[i - 1])

def get_tribo_memo(N: int, memo: List[int]) -> int:
    """
    N : index
    """
    if N == 0:
        return 0
    if N == 1:
        return 0
    if N == 2:
        return 1

    if memo[N] != -1:
        return memo[N]
    else:
        memo[N] = get_tribo_memo(N - 1, memo) + get_tribo_memo(N - 2, memo) + get_tribo_memo(N - 3, memo)
        return memo[N]

def count_753number(K: int) -> int:
    
    d = len(str(K))

    def put(num: str, d: int) ->str:
        if d == 0:
            return num
        else:
            return put(num + "7", d - 1), put(num + "5", d - 1), put(num + "3", d - 1)

def is_partial_sum_memo(array: List[int], i: int, W: int,
                        memo: List[bool], d: int) -> bool:
    if i == 0 and W == 0:
        return True
    if i == 0 and W != 0:
        return False

    if memo[i - 1, W + d - 1] != -1:
        return memo[i - 1, W + d - 1]
    else:
        memo[i - 1, W + d - 1] = is_partial_sum(array, i - 1, W)\
            + is_partial_sum(array, i - 1, W - array[i - 1])
        return memo[i - 1, W + d - 1]