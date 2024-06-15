import unittest
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def fractional_knapsack(capacity, items):
    items.sort(key=lambda x: x.value / x.weight, reverse=True)
    total_value = 0
    total_weight = 0

    for item in items:
        if total_weight + item.weight <= capacity:
            total_weight += item.weight
            total_value += item.value
        else:
            fraction = (capacity - total_weight) / item.weight
            total_value += item.value * fraction
            break

    return total_value

# Test case
items = [Item(60, 10), Item(100, 20), Item(120, 30)]
capacity = 50
print("Fractional Knapsack value:", fractional_knapsack(capacity, items))

class TestKnapsack(unittest.TestCase):

    def test_knapsack_empty(self):
        items = []
        capacity = 50
        result = knapsack_brute_force(capacity, items)
        self.assertEqual(result, set())

    def test_knapsack_single_item_fits(self):
        items = [Item(60, 10)]
        capacity = 50
        result = fractional_knapsack(capacity, items)
        self.assertEqual(result, {0})

    def test_knapsack_single_item_does_not_fit(self):
        items = [Item(60, 60)]
        capacity = 50
        result = fractional_knapsack(capacity, items)
        self.assertEqual(result, set())

    def test_knapsack_multiple_items(self):
        items = [Item(60, 10), Item(100, 20), Item(120, 30)]
        capacity = 50
        result = fractional_knapsack(capacity, items)
        # The optimal set of items is {1, 2} with total value 220
        self.assertEqual(result, {1, 2})

    def test_knapsack_multiple_items_not_optimal(self):
        items = [Item(60, 10), Item(100, 20), Item(120, 30)]
        capacity = 50
        result = fractional_knapsack(capacity, items)
        max_value = sum(items[i].value for i in result)
        # The optimal total value is 220
        self.assertEqual(max_value, 220)

if __name__ == '__main__':
    unittest.main()