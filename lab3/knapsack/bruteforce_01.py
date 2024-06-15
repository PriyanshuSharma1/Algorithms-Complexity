class Item:
    def __init__(self, value, weight):
        self.value=value
        self.weight=weight

def knapsack(capacity,items):
    n=len(items)
    max_value=0
    max_set=set()
    for i in range(2**n):
        s=set()
        value=0
        weight=0
        for j in range(n):
            if (i>>j)%2==1:
                s.add(j)
                value+=items[j].value
                weight+=items[j].weight
        if weight<=capacity and value>max_value:
            max_value=value
            max_set=s
    return max_set