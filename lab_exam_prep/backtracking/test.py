import random
def print(board, n=4):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end="")
        print("\n")
    print("\n")

def isSafe(board, row, col):
    for i in range(col):
        if board[row][i]:
            return False
    i=row
    j=col

    while i>=0 and j>=0:
        if board[i][j]:
            return False
        i=i-1
        j=j-1

    i = row
    j= col

    while i>=0 and j<4:
        if board[i][j]:
            return False
        i=i-1
        j=j+1

    return True

def las(n):
    board=[[0 for i in range(n)]for j in range(n)]
    availColums=[]
    for a in range(n):
        availColums.append(a)
    
    R=0
    while (len(availColums))!=0 and R<n:
        temp=[]
        for i in availColums:
            if isSafe(board,R,i):
                temp.append(i)

            if len(temp)==0:
                return False
            
            rand= random.choice(temp)
            board[R][rand]=1

            R=R+1
            availColums.remove(rand)
        print(board)
        return 1
    
i = 0
for a in range(1000):
    if las(4) == 1:
        i += 1
print(i)
print("Success rate is: ", i/1000)
