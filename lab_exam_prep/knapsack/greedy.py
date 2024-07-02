def fracknap(weights, values,capacity):
    items=[]
    for i in range(len(weights)):
        ratio= values[i]/weights[i]
        item=(ratio, weights[i], values[i])
        items.append(item)

    items.sort(reverse=True, key=lambda x:x[0])

    total_value=0.0
    remaining_capacity=capacity

    for ratio, weight, value in items:
        if weight<=remaining_capacity:
            remaining_capacity=remaining_capacity-weight
            total_value +=value
        
    return total_value

values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
print(fracknap(weights, values, capacity))