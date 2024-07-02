def lcsmemo(P,Q,m,n,memo):
    if m==len(P) or n==len(Q):
        return 0
    
    if memo[m][n] != 0:
        return memo[m][n]
    
    if P[m]==Q[n]:
        memo[m][n]= 1+lcsmemo(P,Q,m+1,n+1,memo)

    else:
        memo[m][n]=max(lcsmemo(P,Q,m+1,n,memo),lcsmemo(P,Q,m,n+1,memo))
    
    return memo[m][n]

Y = "stratosphere"
X = "atmosphere"
memo=[[0 for _ in range(len(Y)+1)]for _ in range(len(X)+1)]
print(lcsmemo(X, Y, 0, 0, memo))

    

