class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        
def fractional_knapsack_greedy(capacity, items):
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
print("Fractional Knapsack value (Greedy):", fractional_knapsack_greedy(capacity, items))
