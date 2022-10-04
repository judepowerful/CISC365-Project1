"""The experiment running entrypoint

Includes:
    experiment_1: Running Experiment 1
    experiment_2: Running Experiment 2
"""

from typing import Dict, Tuple
from search_algorithms import *
from array_generator import *
import time

TEST_SIZE = [1000, 2000, 4000, 8000, 16000]


def experiment_1() -> Dict[int, Tuple[int, int]]:
    """Do experiment 1, return the result for plotting.

    Returns:
        A dictionary, with keys the test size n, and values tuple with (timing of bin, timing of trin).
        The unit of data are in nanoseconds
    """
    results: Dict[int, Tuple[int, int]] = {}
    for n in TEST_SIZE:
        random_array = array_generator(n)
        test_set = random_array * 10

        # Use perf_counter_ns for better timing accuracy
        bin_start_time = time.perf_counter_ns()
        for i in test_set:
            bin_search(random_array, i)
        bin_end_time = time.perf_counter_ns()
        bin_delta = bin_end_time - bin_start_time

        trin_start_time = time.perf_counter_ns()
        for i in test_set:
            trin_search(random_array, i)
        trin_end_time = time.perf_counter_ns()
        trin_delta = trin_end_time - trin_start_time

        results[n] = (bin_delta, trin_delta)

        print(f"Array size: {n},",
              f"binary search running time: {bin_delta / 1e9:0.4f}s,",
              f"trinary search running time: {trin_delta / 1e9:0.4f}s,",
              f"{'binary search' if bin_delta < trin_delta else 'trinary search'}",
              f"is quicker, with {abs(bin_delta - trin_delta) / 1e9:0.4f}s")
    return results


def experiment_2() -> Dict[int, Tuple[int, int]]:
    """Do experiment 2, return the result for plotting.

    Returns:
        A dictionary, with keys the test size n, and values tuple with (timing of bin, timing of trin).
        The unit of data are in nanoseconds
    """
    results: Dict[int, Tuple[int, int]] = {}
    for n in TEST_SIZE:
        random_array = array_generator(n, 'even')
        test_set = array_generator(10*n, 'odd', False)

        # Use perf_counter_ns for better timing accuracy
        bin_start_time = time.perf_counter_ns()
        for i in test_set:
            bin_search(random_array, i)
        bin_end_time = time.perf_counter_ns()
        bin_delta = bin_end_time - bin_start_time

        trin_start_time = time.perf_counter_ns()
        for i in test_set:
            trin_search(random_array, i)
        trin_end_time = time.perf_counter_ns()
        trin_delta = trin_end_time - trin_start_time

        results[n] = (bin_delta, trin_delta)

        print(f"Array size: {n},",
              f"binary search running time: {bin_delta / 1e9:0.4f}s,",
              f"trinary search running time: {trin_delta / 1e9:0.4f}s,",
              f"{'binary search' if bin_delta < trin_delta else 'trinary search'}",
              f"is quicker, with {abs(bin_delta - trin_delta) / 1e9:0.4f}s")
    return results


if __name__ == '__main__':
    print("start testing for search functions")
    test_array = [0, 2, 12, 13, 16, 28, 30, 32, 36,
                  37, 37, 38, 47, 47, 48, 55, 75, 75, 78, 79]
    for num in test_array:
        assert test_array[bin_search(test_array, num)] == num
        assert test_array[trin_search(test_array, num)] == num
    not_existing = [-5, -1, 1, 40, 60, 80, 10000]
    for num in not_existing:
        assert bin_search(test_array, num) == -1
        assert trin_search(test_array, num) == -1
    print("No exception arise, suggesting our search function are working well")
    print("=============================================")
    print("Now Running Experiment 1")
    print("Raw data from experiment 1:", experiment_1())
    print("=============================================")
    print("Now Running Experiment 2")
    print("Raw data from experiment 2:", experiment_2())
