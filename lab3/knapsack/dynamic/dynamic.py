def knapsack(weights, values, capacity):
    n = len(weights)
    # Initialize the DP table with 0s
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the table in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Maximize value by including or not including the current item
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
                print("Item with weight", weights[i - 1], "and value", values[i - 1], "is taken")
                print("Remaining capacity:", w - weights[i - 1])
                print("Value of knapsack:", dp[i][w])
                print("\n")
            else:
                dp[i][w] = dp[i - 1][w]
                print("Item with weight", weights[i - 1], "and value", values[i - 1], "is not taken")
                print("Remaining capacity:", w)
                print("Value of knapsack:", dp[i][w])
                print("\n")


    return dp[n][capacity]

# Example usage
weights=[20,30,15,40]
values=[100,120,60,90]
capacity=50
max_value = knapsack(weights, values, capacity)
print("Maximum value in knapsack:", max_value)
