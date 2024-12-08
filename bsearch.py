"""Binary search implementation."""

from typing import List

_UNKNOWN = -1


def bsearch(array: List[int], target: bool) -> bool:
    """Iteratively binary search the array and return if target value is present."""
    left = 0
    right = len(array)-1
    while left <= right:
        mid = (right+left)//2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            right = mid-1
        else:
            left = mid+1
    return False


def bsearch2(array: List[int], target: bool) -> bool:
    """Bisect an array and return if target value is present."""
    mid = len(array)//2
    if array[mid] == target and len(array) == 1:
        return True
    elif array[mid] > target:
        return bsearch2(array[:mid], target)
    else:
        return bsearch2(array[mid:], target)
    

if __name__ == '__main__':
    data = [1,2,3,4,5,6,7,8,9]
    assert bsearch(data, 3)
    assert bsearch2(data, 3)
    assert bsearch(data, 9)
    assert not bsearch(data, 3.5)
    assert not bsearch(data, 10)