class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        
def knapsack_dp(capacity, items):
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if items[i - 1].weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - items[i - 1].weight] + items[i - 1].value)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# Test case
items = [Item(60, 10), Item(100, 20), Item(120, 30)]
capacity = 50
print("0/1 Knapsack value (Dynamic Programming):", knapsack_dp(capacity, items))
