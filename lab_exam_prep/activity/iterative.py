def act(s,f,n):
    if n==0:
        return[]
    selected=[]
    selected.append((s[0],f[0]))
    for i in range(n):
        if s[i] > selected[-1][1]:
             selected.append((s[i],f[i]))
    
    print(selected)

s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
f = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
act(s,f,len(s))

if n==0:
    return []

selected=[]
selected.append((s[0],f[0]))

for i in range(n):
    if s[i]>selected[-1][1]:
        selected.append((s[i],f[i]))
        