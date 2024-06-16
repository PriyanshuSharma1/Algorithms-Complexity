import unittest
from lab3.knapsack.bruteforce.bruteforce import fractional_knapsack

class TestFractionalKnapsack(unittest.TestCase):
    def test_knapsack(self):
        weights = [2, 3, 4, 5]
        values = [3, 4, 5, 6]
        capacity = 5
        max_value = fractional_knapsack(weights, values, capacity)
        self.assertAlmostEqual(max_value, 7.0)

    def test_knapsack_empty(self):
        weights = []
        values = []
        capacity = 5
        max_value = fractional_knapsack(weights, values, capacity)
        self.assertAlmostEqual(max_value, 0)

    def test_knapsack_zero_capacity(self):
        weights = [2, 3, 4, 5]
        values = [3, 4, 5, 6]
        capacity = 0
        max_value = fractional_knapsack(weights, values, capacity)
        self.assertAlmostEqual(max_value, 0)

    def test_knapsack_all_items(self):
        weights = [1, 1, 1, 1]
        values = [1, 1, 1, 1]
        capacity = 4
        max_value = fractional_knapsack(weights, values, capacity)
        self.assertAlmostEqual(max_value, 4)
if __name__ == '__main__':
    unittest.main()