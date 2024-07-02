def knapsack(prof, wt, cap):
    return knapsacksol(prof, wt, cap,0)

def knapsacksol(prof,wt,cap,current):
    if current>=len(prof) or cap<=0:
        return 0
    prof1=0
    if wt[current]<=cap:
        prof1=prof[current]+knapsacksol(prof, wt, cap-wt[current],current+1)
    
    prof2=knapsacksol(prof,wt,cap,current+1)

    return max(prof1,prof2)

weights = [2, 3, 6, 5]
values = [1, 0, 5, 8]
capacity = 8
kn=knapsack(values,weights,capacity)
print(kn)
