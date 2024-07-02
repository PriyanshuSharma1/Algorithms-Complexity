items=((0,10,4),(1,20,6),(2,11,3))
def powerset(items):
    res=[[]]
    for item in items:
        newset=[r+[item] for r in res]
        res.extend(newset)
    
    return res

def knapsack(items, maxweight):
    knapsack=[]
    bestval=0
    bestwt=0
    for item in powerset(items):
        sval= sum(m[1] for m in item)
        swt= sum(m[2] for m in item)

        if sval>bestval and swt<maxweight:
            bestval=sval
            bestwt=swt
            knapsack=item
        
    return knapsack, bestval,bestwt


print(knapsack(items,10))