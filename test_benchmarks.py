"""Tests for the benchmarks."""

import unittest
from benchmarks import linear_search, measure_execution_time, generate_random_array
from bsearch import bsearch

class TestBenchmarks(unittest.TestCase):
    def test_linear_search_vs_bsearch_small(self):
        array = generate_random_array(100)
        target = 50
        linear_time = measure_execution_time(linear_search, array, target)
        bsearch_time = measure_execution_time(bsearch, array, target)
        self.assertLess(bsearch_time, linear_time)

    def test_linear_search_vs_bsearch_medium(self):
        array = generate_random_array(1000)
        target = 500
        linear_time = measure_execution_time(linear_search, array, target)
        bsearch_time = measure_execution_time(bsearch, array, target)
        self.assertLess(bsearch_time, linear_time)

    def test_linear_search_vs_bsearch_large(self):
        array = generate_random_array(10000)
        target = 5000
        linear_time = measure_execution_time(linear_search, array, target)
        bsearch_time = measure_execution_time(bsearch, array, target)
        self.assertLess(bsearch_time, linear_time)

if __name__ == '__main__':
    unittest.main()
