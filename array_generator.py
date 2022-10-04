"""The array generator used by Project 1

Includes:
    array_generator: The function to generate an array for the experiment.
    bubble_sort: An implementation of bubble sort, for the preliminary concept testing.
    merge_sort: An implementation of merge sort, for the sake of speed.
    merge: The merge function used by merge_sort.
"""

import random
from typing import Literal, Optional


def array_generator(n: int, req: Optional[Literal["even", "odd"]] = None, doSort: bool = True) -> list[int]:
    """Generates an array of length n.

    Args:
        n (int): The size of array needed.
        req ("even" or "odd", optional):
            If we require the generated array to be even or odd number only, use this parameter.
            Defaults to None, i.e no requirement.
        doSort (bool, optional):
            If we need the generated array to be sorted ascending.
            Defaults to True.

    Returns:
        Generated list satisfying given requirements, with every element in the range of 0 - 4*n
    """
    if req is None:
        generated_array = [random.randint(0, 4*n) for _ in range(n)]
    else:
        f = (lambda x: 2 * x) if req == "even" else (lambda x: 2 * x + 1)
        generated_array = [f(random.randint(0, 2*n)) for _ in range(n)]
    # sort the array
    if doSort:
        # Define the default sorting method. Defaults to Merge sort.
        sort = merge_sort
        sort(generated_array)
    return generated_array


def bubble_sort(array: list[int]):
    """Bubble Sort loop implementation. Sorting array in ascending order.

    Args:
        array (list of int): The list to sort with.
    """
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


def merge_sort(array: list[int], first: Optional[int] = None, last: Optional[int] = None):
    """Merge Sort recursive implementation. Sorting array in ascending order.

    Args:
        array (list of int): The list to sort with.
        first (int):  Index of the start of sort interval.
                        Left empty or specify Null will defaults to 0.
        last (int):   Index of the end of sort interval.
                        Left empty or specify Null will defaults to len(A).
    """
    # Set the default value of search interval.
    if first is None:
        first = 0
    if last is None:
        last = len(array)

    # if the sub-array to sort has length 1, we halt recursion.
    if last - first <= 1:
        return
    mid = (first + last) // 2
    merge_sort(array, first, mid)
    merge_sort(array, mid, last)
    merge(array, first, mid, last)


def merge(array: list[int], first: int, mid: int, last: int):
    """Merge the array[first:mid] and array[mid+1:last] with ascending order

    Args:
        array (list of int): The list to merge with. Assuming array[first:mid] and array[mid+1:last] are already sorted.
        first (int):  Index of the start of merge interval.
        mid (int):    Index of the midpoint of merge interval.
        last (int):   Index of the end of merge interval.
    """
    temp: list = []
    i, j = first, mid

    # Pick elements of array[first:mid] and array[mid+1:last] into temp by ascending order
    while i < mid and j < last:
        if array[i] <= array[j]:
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1

    # Make sure every element are appended.
    # Notice that former loop guarantees that one of left or right sub-array must be exhausted.
    # So we will only execute one of following while loop.
    while i < mid:
        temp.append(array[i])
        i += 1
    while j < last:
        temp.append(array[j])
        j += 1
    assert(len(temp) == last - first)

    # Copy the elements from temp to array
    for i in range(len(temp)):
        array[first + i] = temp[i]
