"""Microbenchmarks for search algorithms."""

import time
from typing import List
import random
from bsearch import bsearch

def linear_search(array: List[int], target: int) -> bool:
    """Linearly search the array and return if target value is present."""
    for element in array:
        if element == target:
            return True
    return False

def measure_execution_time(func, array: List[int], target: int) -> float:
    """Measures the execution time of a function."""
    start_time = time.time()
    func(array, target)
    end_time = time.time()
    return end_time - start_time

def generate_random_array(size: int) -> List[int]:
    """Generates a random array of a given size."""
    array = []
    for _ in range(size):
        array.append(random.randint(0, size))
    return array

def run_benchmarks():
    """Runs benchmarks for linear search and bsearch."""
    sizes = [100, 1000, 10000]
    for size in sizes:
      array = generate_random_array(size)
      target = random.randint(0, size)
      linear_time = measure_execution_time(linear_search, array, target)
      bsearch_time = measure_execution_time(bsearch, array, target)
      print(f"Size: {size}, Linear Search Time: {linear_time:.6f}s, Binary Search Time: {bsearch_time:.6f}s")

if __name__ == '__main__':
  run_benchmarks()

def measure_execution_time(func, array: List[int], target: int) -> float:
    """Measures the execution time of a function."""
    start_time = time.time()
    func(array, target)
    end_time = time.time()
    return end_time - start_time

def generate_random_array(size: int) -> List[int]:
    """Generates a random array of a given size."""
    array = []
    for _ in range(size):
        array.append(random.randint(0, size))
    return array

def run_benchmarks():
    """Runs benchmarks for linear search and bsearch."""
    sizes = [100, 1000, 10000]
    for size in sizes:
      array = generate_random_array(size)
      target = random.randint(0, size)
      linear_time = measure_execution_time(linear_search, array, target)
      bsearch_time = measure_execution_time(bsearch, array, target)
      print(f"Size: {size}, Linear Search Time: {linear_time:.6f}s, Binary Search Time: {bsearch_time:.6f}s")

if __name__ == '__main__':
  run_benchmarks()
