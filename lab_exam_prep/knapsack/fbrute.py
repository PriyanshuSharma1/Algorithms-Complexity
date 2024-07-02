def fractional_knapsack(weights, values, capacity):
    items = []
    for i in range(len(weights)):
        ratio = values[i] / weights[i]
        items.append((ratio, weights[i], values[i]))

    items.sort(reverse=True, key=lambda x: x[0])

    total_value = 0.0
    remaining_capacity = capacity

    for ratio, weight, value in items:
        if remaining_capacity == 0:
            break
        if weight <= remaining_capacity:
            remaining_capacity -= weight
            total_value += value
        else:
            fraction = remaining_capacity / weight
            total_value += value * fraction
            remaining_capacity = 0

    return total_value

# Example usage:
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
print(fractional_knapsack(weights, values, capacity))  # Output: 240.0
