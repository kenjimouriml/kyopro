from typing import List, Tuple
import itertools
import numpy as np

def linear_search(num_list: List[int], target: int) -> Tuple[bool, int]:

    if type(target) is not int:
        return False, -1

    flag = False
    idx = -1
    for i in range(len(num_list)):
        if target == num_list[i]:
            flag = True
            idx = i
            break

    return flag, idx
    
def set_search(num_list: List[int], target: int) -> bool:

    if type(target) is not int:
        return False

    return target in set(num_list)


def get_min_value(num_list: List[float]) -> float:
    """
    linear search
    """

    min_value = num_list[0]
    idx = 0
    for i in range(len(num_list)):
        if num_list[i] <= min_value:
            min_value = num_list[i]
            idx = i

    return min_value, idx


def get_min_pair(num_list1: List[int], num_list2: List[int], K: int) -> int:
    """
    by linear search
    """
    min_val = 2000000000
    flag = False
    for i in range(len(num_list1)):
        for j in range(len(num_list2)):
            val = num_list1[i] + num_list2[j]
            if val >= K:
                if val <= min_val:
                    min_val = val
                    flag = True

    return min_val * flag + K * (1- flag)


def is_partial_sum(num_list: List[int], W: int) -> bool:
    """
    by linear search O(N2^N)
    """
    N = len(num_list)
    flag = False
    for i in range(0, 2**N):
        i_bin = bin(i)
        total = 0
        for j in range(0, len(i_bin) - 2):
            if i_bin[j + 2] == "1":
                total += num_list[j]

        if total == W:
            flag = True
            break

    return flag

def count_divs(num_list: List[int]) -> int:

    min_div_counter = 20000000
    
    for i in range(0, len(num_list)):
        j = 1
        while 2**j <= num_list[i]:
            if num_list[i] % 2**j == 0:
                j += 1
            else:
                break

        if min_div_counter >= j - 1:
            min_div_counter = j - 1               

    return min_div_counter

def count_sum_variations(N: int, K: int) -> int:

    counter = 0
    for i in range(0, K + 1):
        for j in range(i, K + 1):
            if N -i >= 2 * j and N - i - j <= K:
                counter += 1

    return counter

def sum_Ndigit_numbers(num: str) -> int:
    """
    linear search O(N2^N)
    """

    N = len(num)
    total = 0
    for i in range(2 ** (N - 1)):
        i_bin = format(i, "b")
        i_bin = "".join("0" for _ in range(N - 1 - len(i_bin))) + i_bin
        
        idx_last = 0
        for j in range(N - 1):
            if i_bin[j] == "1":
                total += int(num[idx_last:j + 1])
                idx_last = j + 1

        total += int(num[idx_last:])

    return total