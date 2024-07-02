
def fractional_knapsack(weights, values, capacity):
    # Compute value-to-weight ratios and store items with their ratios
    # Initialize an empty list to store the tuples
    items = []

    # Iterate over the indices of the weights list
    for i in range(len(weights)):
    # Calculate the ratio of value to weight
        ratio = values[i] / weights[i]

        # Create a tuple with the ratio, weight, and value
        item = (ratio, weights[i], values[i])

        # Append the tuple to the items list
        items.append(item)


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
