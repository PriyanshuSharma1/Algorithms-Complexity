import unittest
class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight

def fractional_knapsack(weights, values, capacity):
    items = [Item(weights[i], values[i]) for i in range(len(weights))]
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)

    total_value = 0.0
    for item in items:
        if capacity == 0:
            break
        if item.weight <= capacity:
            # Take the whole item
            capacity -= item.weight
            total_value += item.value
        else:
            # Take a fraction of the item
            total_value += item.value * (capacity / item.weight)
            capacity = 0

    return total_value
