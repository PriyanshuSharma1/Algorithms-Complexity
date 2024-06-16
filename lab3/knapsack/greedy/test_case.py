import unittest
from greedy import fractional_knapsack 

class TestFractionalKnapsack(unittest.TestCase):
    def test_knapsack(self):
        weights=[30,20,40,36,25]
        values=[60,100,120,80,60]
        capacity=65
        max_value=fractional_knapsack(weights,values,capacity)
        self.assertAlmostEqual(max_value, 232.0)
    
    def test_knapsack_empty(self):
        weights = []
        values = []
        capacity = 5
        max_value = fractional_knapsack(weights, values, capacity)
        self.assertAlmostEqual(max_value, 0)

    def test_knapsack_zero_capacity(self):
        weights = [20, 36, 47, 55]
        values = [19, 40, 33, 16]
        capacity = 0
        max_value = fractional_knapsack(weights, values, capacity)
        self.assertAlmostEqual(max_value, 0)

    def test_knapsack_all_items(self):
        weights = [10, 20, 60, 30]
        values = [40, 80, 100, 55]
        capacity = 120
        max_value = fractional_knapsack(weights, values, capacity)
        self.assertAlmostEqual(max_value, 275.0)

if __name__ == '__main__':
    unittest.main()