def getDividers(n):
    """
    input: integer
    return : the list of dividers of the above integers
    """

    lower_dividers, upper_dividers = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_dividers.append(i)
            if i != n // i:
                upper_dividers.append(n // i)

        i += 1

    return lower_dividers + upper_dividers[::-1]


def binary_search(arr, target):
    """
    return max value less than target
    """

    left = 0
    right = len(arr) - 1
    while right - left >= 0:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid, arr[mid]
        elif arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1

    return right, arr[right]


def binary_search_v2(arr, target):
    """
    return min value greater than target
    """

    left = 0
    right = len(arr) - 1
    while right - left >= 0:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid, arr[mid]
        elif arr[mid] < target:
            right = mid - 1
        elif arr[mid] > target:
            left = mid + 1

    return right, arr[right]
