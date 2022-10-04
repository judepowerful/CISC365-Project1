"""The search algorithms used by Project 1, modified for the sake of convenience

Author:
    Yu Peng(Code), Somion Tian(Comments)

Includes:
    trin_search: Trinary search algorithm implementation
    bin_search:  Binary search algorithm implementation
"""

from typing import Any, Optional


def trin_search(A: list, target: Any, first: Optional[int] = None, last: Optional[int] = None) -> int:
    """Divide list A into three parts and search for target recursively.

    Author:
        Yu Peng

    Args:
        A (list):     The list to search with.
        target (Any): The target object to search for.
        first (int):  Index of the start of search interval.
                        Left empty or specify Null will defaults to 0.
        last (int):   Index of the end of search interval.
                        Left empty or specify Null will defaults to len(A).

    Returns:
        int: Index of target if it presents in A, -1 if it is not present in A
    """
    # Set the default value of search interval.
    if first is None:
        first = 0
    if last is None:
        last = len(A)

    # returns -1 if target is not present in A
    if first > last:
        return -1

    one_third = first + (last - first) // 3
    two_thirds = first + 2 * (last - first) // 3

    # prevent index out of range error
    if one_third == len(A) or two_thirds == len(A):
        return -1

    if A[one_third] == target:
        return one_third
    elif A[one_third] > target:
        # search the left-hand third
        return trin_search(A, target, first, one_third - 1)
    elif A[two_thirds] == target:
        return two_thirds
    elif A[two_thirds] > target:
        # search the middle third
        return trin_search(A, target, one_third + 1, two_thirds - 1)
    else:
        # search the right-hand third
        return trin_search(A, target, two_thirds + 1, last)


def bin_search(A: list, target: Any, first: Optional[int] = None, last: Optional[int] = None) -> int:
    """Use binary search to search for target recursively.

    Author:
        Yu Peng

    Args:
        A (list):     The list to search with.
        target (Any): The target object to search for.
        first (int):  Index of the start of search interval.
                        Left empty or specify Null will defaults to 0.
        last (int):   Index of the end of search interval.
                        Left empty or specify Null will defaults to len(A).

    Returns:
        int: Index of target if it presents in A, -1 if it is not present in A
    """
    # Set the default value of search interval.
    if first is None:
        first = 0
    if last is None:
        last = len(A)

    # returns -1 if target is not present in A
    if first > last:
        return -1

    mid = (first + last) // 2

    # prevent index out of range error
    if mid == len(A):
        return -1

    if A[mid] == target:
        return mid
    elif A[mid] > target:
        return bin_search(A, target, first, mid - 1)
    else:
        return bin_search(A, target, mid + 1, last)
