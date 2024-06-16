import unittest
from knapsack01 import brute_force_knapsack
class TestKnapsack(unittest.TestCase):
    def test_knapsack(self):
        weights = [2, 3, 4, 5]
        values = [3, 4, 5, 6]
        capacity = 5
        max_value, max_combination = brute_force_knapsack(weights, values, capacity)
        self.assertEqual(max_value, 7)
        self.assertEqual(max_combination, [0, 1])

    def test_knapsack_empty(self):
        weights = []
        values = []
        capacity = 5
        max_value, max_combination = brute_force_knapsack(weights, values, capacity)
        self.assertEqual(max_value, 0)
        self.assertEqual(max_combination, [])

    def test_knapsack_zero_capacity(self):
        weights = [2, 3, 4, 5]
        values = [3, 4, 5, 6]
        capacity = 0
        max_value, max_combination = brute_force_knapsack(weights, values, capacity)
        self.assertEqual(max_value, 0)
        self.assertEqual(max_combination, [])

    def test_knapsack_all_items(self):
        weights = [1, 1, 1, 1]
        values = [1, 1, 1, 1]
        capacity = 4
        max_value, max_combination = brute_force_knapsack(weights, values, capacity)
        self.assertEqual(max_value, 4)
        self.assertEqual(set(max_combination), set([0, 1, 2, 3]))

if __name__ == '__main__':
    unittest.main()
