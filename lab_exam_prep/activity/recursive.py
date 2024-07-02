def act(s,f,k,n,selected):
    if n==0:
        return[]
    selected.append((s[k],f[k]))
    
    m=k+1
    while m<n and s[m]<f[k]:
        m=m+1
    if m<n:
        act(s,f,m,n,selected)
    
    return selected

s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
f = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
selected = []
act(s,f,0,len(s),selected)
print(selected)

def act(s,f,k,n selected):
    if n==0:
        return []
    selected.append((s[k],f[k]))

    m=k+1
    while m<n and s[m]<f[k]:
        m=m+1
    
    if m<n:
        act(s,f,m,n,selected)    
    
    return selected



    
    

