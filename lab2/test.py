import unittest
from generatearray import generate_random_array, generate_sorted_array, generate_reverse_sorted_array
from mergesort import merge_sort
from quicksort import quick_sort

class TestSortingAlgorithms(unittest.TestCase):

    def test_merge_sort_random(self):
        arr = generate_random_array(100)
        sorted_arr = sorted(arr)
        self.assertEqual(merge_sort(arr), sorted_arr)

    def test_quick_sort_random(self):
        arr = generate_random_array(100)
        sorted_arr = sorted(arr)
        self.assertEqual(quick_sort(arr), sorted_arr)

    def test_merge_sort_sorted(self):
        arr = generate_sorted_array(100)
        sorted_arr = sorted(arr)
        self.assertEqual(merge_sort(arr), sorted_arr)

    def test_quick_sort_sorted(self):
        arr = generate_sorted_array(100)
        sorted_arr = sorted(arr)
        self.assertEqual(quick_sort(arr), sorted_arr)

    def test_merge_sort_reverse_sorted(self):
        arr = generate_reverse_sorted_array(100)
        sorted_arr = sorted(arr)
        self.assertEqual(merge_sort(arr), sorted_arr)

    def test_quick_sort_reverse_sorted(self):
        arr = generate_reverse_sorted_array(100)
        sorted_arr = sorted(arr)
        self.assertEqual(quick_sort(arr), sorted_arr)

    def test_merge_sort_empty(self):
        self.assertEqual(merge_sort([]), [])

    def test_quick_sort_empty(self):
        self.assertEqual(quick_sort([]), [])

    def test_merge_sort_single_element(self):
        self.assertEqual(merge_sort([1]), [1])

    def test_quick_sort_single_element(self):
        self.assertEqual(quick_sort([1]), [1])

if __name__ == "__main__":
    unittest.main()
