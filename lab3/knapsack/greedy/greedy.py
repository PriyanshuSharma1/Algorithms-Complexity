
def fractional_knapsack(weights, values, capacity):
    # Compute value-to-weight ratios and store items with their ratios
    items = [(values[i] / weights[i], weights[i], values[i]) for i in range(len(weights))]
    
    # Sort items by value-to-weight ratio in descending order
    items.sort(reverse=True, key=lambda item: item[0])
    
    total_value = 0.0
    remaining_capacity = capacity
    
    # Iterate through sorted items
    for ratio, weight, value in items:
        if remaining_capacity == 0:
            break
        if weight <= remaining_capacity:
            # Take the whole item
            remaining_capacity -= weight
            total_value += value
            print("Item with weight", weight, "and value", value, "is taken")
            print("Remaining capacity:", remaining_capacity)
        else:
            # Take a fraction of the item
            fraction = remaining_capacity / weight
            total_value += value * fraction
            remaining_capacity = 0
            print("Item with weight", weight, "and value", value, "is taken fractionally")
            print("Remaining capacity:", remaining_capacity)
            print("\n")

    
    return total_value

# Example usage
weights=[30,20,40,36,25]
values=[60,100,120,80,60]
capacity=65
max_value = fractional_knapsack(weights, values, capacity)
print("Maximum value in knapsack:", max_value)
print("\n")
