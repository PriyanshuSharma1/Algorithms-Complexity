def brute_force_knapsack(weights, values, capacity):
    n = len(weights)  # number of items
    max_value = 0  # maximum value that can be carried
    max_combination = []  # list of items that can be carried in the knapsack

    # Generate all possible combinations of items
    for i in range(2**n):
        combination = []
        total_weight = 0
        total_value = 0

        # Check each toy to see if it's picked in this combination
        for j in range(n):
            # If the j-th bit of i is 1, it means pick the j-th toy
            if (i >> j) & 1:
                combination.append(j)  # Add the toy to the combination
                total_weight += weights[j]  # Add its weight
                total_value += values[j]  # Add its value

        # Check if the combination is valid and update the maximum value
        if total_weight <= capacity and total_value > max_value:
            max_value = total_value
            max_combination = combination

    return max_value, max_combination
